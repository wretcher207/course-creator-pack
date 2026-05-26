"""Refund De-escalator Agent — refund request to tactful reply."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.client import chat, extract_json

PROMPT_FILE = Path(__file__).parent / "system_prompt.md"


def respond(request_text: str, context: str = "") -> dict:
    system_prompt = PROMPT_FILE.read_text(encoding="utf-8")
    user_msg = (
        f"REFUND REQUEST:\n{request_text}\n\n"
        f"CONTEXT (optional):\n{context or '(none)'}"
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_msg},
    ]
    raw = chat(messages, max_tokens=1400, temperature=0.4)
    parsed = extract_json(raw)
    if parsed is None:
        return {"_error": "Model did not return parseable JSON", "_raw": raw}
    return parsed


def _read_block(label: str) -> str:
    print(f"{label} (end with a line containing only END):")
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def _section(title: str, body: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)
    print(body)


def _print_result(r: dict) -> None:
    if "_error" in r:
        print("\n[!] Model output was not parseable JSON:")
        print(r["_error"])
        print("\nRaw output:")
        print(r["_raw"])
        return

    print()
    print(f"REAL REASON:    {r.get('real_reason')}")
    print(f"BUYER STATE:    {r.get('buyer_state')}")
    print(f"RECOMMENDATION: {r.get('recommendation')}")
    print(f"WHY:            {r.get('recommendation_reason')}")

    _section("DRAFT REPLY", r.get("draft_reply", ""))
    _section("IF THEY PUSH BACK", r.get("if_they_push_back", ""))
    _section("INTERNAL NOTE", r.get("internal_note", ""))

    flags = r.get("policy_flags") or []
    if flags:
        _section("[!] POLICY FLAGS", "\n".join(f"  - {f}" for f in flags))
    print()


def main() -> None:
    print("=== Refund De-escalator Agent ===")
    print("Powered by free OpenRouter models. Costs $0 to test.\n")

    req = _read_block("Paste the refund request from the buyer")
    if not req:
        print("No request given. Exiting.")
        return
    print()
    ctx = _read_block(
        "Optional context (product name, refund policy, days since purchase) — or just type END"
    )

    print("\nThinking...")
    _print_result(respond(req, ctx))


if __name__ == "__main__":
    main()
