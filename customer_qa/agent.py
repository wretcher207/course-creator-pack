"""Customer Q&A Agent — pre-purchase question to specific reply."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.client import chat, extract_json

PROMPT_FILE = Path(__file__).parent / "system_prompt.md"


def answer(question: str, product_context: str) -> dict:
    system_prompt = PROMPT_FILE.read_text(encoding="utf-8")
    user_msg = (
        f"BUYER QUESTION:\n{question}\n\n"
        f"PRODUCT CONTEXT (creator's source of truth):\n{product_context}"
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_msg},
    ]
    raw = chat(messages, max_tokens=1200, temperature=0.4)
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
    print(f"INTENT:    {r.get('question_intent')}")
    print(f"FIT:       {r.get('fit_assessment')}")
    print(f"WHY:       {r.get('fit_reason')}")

    _section("DRAFT REPLY", r.get("draft_reply", ""))

    no_fit = r.get("honest_no_fit_reply", "").strip()
    if no_fit:
        _section("ALT REPLY (use if not a fit)", no_fit)

    fu = r.get("follow_up_question", "").strip()
    if fu:
        _section("FOLLOW-UP QUESTION FOR YOU", fu)

    cp = r.get("common_pattern", "").strip()
    if cp:
        _section("PATTERN NOTE", cp)
    print()


def main() -> None:
    print("=== Customer Q&A Agent ===")
    print("Powered by free OpenRouter models. Costs $0 to test.\n")

    q = _read_block("Paste the buyer's question")
    if not q:
        print("No question given. Exiting.")
        return
    print()
    ctx = _read_block(
        "Paste your product details (what it is, who it is for, what's included, "
        "what's NOT included, price, format, refund policy, level required)"
    )
    if not ctx:
        print("No product context given. Without context the agent will not answer well. Exiting.")
        return

    print("\nThinking...")
    _print_result(answer(q, ctx))


if __name__ == "__main__":
    main()
