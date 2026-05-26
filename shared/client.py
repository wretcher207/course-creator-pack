"""Tiny LLM client. No SDK, just requests.

Provider auto-detect: if a MINIMAX_API_KEY is in the environment, calls run on
MiniMax (MiniMax-M2). Otherwise they run on OpenRouter (with the free-model
fallback chain). Lets one machine run on MiniMax with zero config while the
product still works for a buyer who only has an OpenRouter key.
"""
import json
import os
import re
import sys
import requests

from .keyloader import load_api_key


def extract_json(text: str) -> dict | None:
    """Try hard to pull a JSON object out of an LLM response.
    Handles: bare JSON, ```json fenced blocks, JSON embedded in prose,
    and reasoning-model output that wraps JSON in chain-of-thought.
    Returns None if no parseable object is found.
    """
    if not text:
        return None
    text = text.strip()

    # Reasoning models (MiniMax-M2, etc.) emit a <think>...</think> block before
    # the answer. Strip complete blocks; if one was opened but truncated (no
    # close), drop everything from it on (there is no JSON inside the thinking).
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    if "<think>" in text:
        text = text.split("<think>", 1)[0].strip()

    # strict=False tolerates literal control chars (newlines, tabs) inside string
    # values, which reasoning models sometimes emit in long multi-line fields.
    try:
        return json.loads(text, strict=False)
    except json.JSONDecodeError:
        pass

    fenced = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    for block in fenced:
        try:
            return json.loads(block, strict=False)
        except json.JSONDecodeError:
            continue

    first = text.find("{")
    last = text.rfind("}")
    if first != -1 and last > first:
        candidate = text[first : last + 1]
        try:
            return json.loads(candidate, strict=False)
        except json.JSONDecodeError:
            pass

    return None


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

MINIMAX_URL = "https://api.minimax.io/v1/chat/completions"
MINIMAX_MODEL = "MiniMax-M2"


def _chat_minimax(messages: list[dict], api_key: str, max_tokens: int, temperature: float) -> str:
    """Call MiniMax (OpenAI-compatible). MiniMax-M2 is a reasoning model: it emits
    a <think>...</think> block inline and spends tokens thinking. Enforce a token
    floor (per-agent budgets were tuned for non-reasoning models), retry once with
    more room if the reply was truncated (finish_reason 'length'), and strip the
    think block from the returned text."""
    max_tokens = max(max_tokens, 4000)
    content = ""
    for attempt in range(2):
        r = requests.post(
            MINIMAX_URL,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": MINIMAX_MODEL,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            },
            timeout=120,
        )
        if r.status_code != 200:
            raise RuntimeError(f"MiniMax {MINIMAX_MODEL} -> HTTP {r.status_code}: {r.text[:200]}")
        choice = r.json()["choices"][0]
        msg = choice.get("message", {})
        content = msg.get("content") or msg.get("reasoning_content") or ""
        if choice.get("finish_reason") == "length" and attempt == 0:
            max_tokens = min(max_tokens * 2, 16000)
            continue
        break
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
    if not content:
        raise RuntimeError("MiniMax returned empty content")
    return content

FREE_MODELS = [
    "meta-llama/llama-3.3-70b-instruct:free",
    "openai/gpt-oss-120b:free",
    "openai/gpt-oss-20b:free",
    "z-ai/glm-4.5-air:free",
    "qwen/qwen3-next-80b-a3b-instruct:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    "openrouter/free",
]


def chat(
    messages: list[dict],
    model: str = FREE_MODELS[0],
    max_tokens: int = 800,
    temperature: float = 0.5,
    fallback: bool = True,
    referer: str = "https://github.com/dead-pixel-design/course-creator-pack",
    title: str = "course-creator-pack",
) -> str:
    """Return the assistant text content.

    If MINIMAX_API_KEY is set, route to MiniMax (MiniMax-M2). Otherwise call
    OpenRouter, and if fallback=True try the free models in turn on any error.
    """
    mm_key = os.environ.get("MINIMAX_API_KEY")
    if mm_key:
        return _chat_minimax(messages, mm_key, max_tokens, temperature)

    api_key = load_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": referer,
        "X-Title": title,
    }

    models_to_try = [model]
    if fallback:
        for m in FREE_MODELS:
            if m not in models_to_try:
                models_to_try.append(m)

    last_err: Exception | None = None
    for m in models_to_try:
        body = {
            "model": m,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        try:
            r = requests.post(OPENROUTER_URL, headers=headers, json=body, timeout=60)
            if r.status_code == 200:
                data = r.json()
                msg = data["choices"][0]["message"]
                content = msg.get("content")
                if not content:
                    content = msg.get("reasoning") or msg.get("reasoning_content") or ""
                if not content:
                    last_err = RuntimeError(f"{m} returned empty content")
                    print(f"[{m} returned empty content, trying next]", file=sys.stderr)
                    continue
                if m != model:
                    print(f"[fell back to {m}]", file=sys.stderr)
                return content
            else:
                last_err = RuntimeError(f"{m} -> HTTP {r.status_code}: {r.text[:200]}")
                print(f"[{m} failed: {r.status_code}, trying next]", file=sys.stderr)
                continue
        except requests.RequestException as e:
            last_err = e
            print(f"[{m} network error: {e}, trying next]", file=sys.stderr)
            continue

    raise RuntimeError(f"All free models failed. Last error: {last_err}")
