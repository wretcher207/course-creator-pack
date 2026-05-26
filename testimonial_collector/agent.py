"""Testimonial Collector Agent — buyer context to ask + 2 follow-ups."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.client import chat, extract_json

PROMPT_FILE = Path(__file__).parent / "system_prompt.md"


def make_ask(buyer_context: str) -> dict:
    system_prompt = PROMPT_FILE.read_text(encoding="utf-8")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"BUYER CONTEXT:\n\n{buyer_context}"},
    ]
    raw = chat(messages, max_tokens=1600, temperature=0.5)
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
    print(f"BUYER STAGE: {r.get('buyer_stage_read')}")
    print(f"TIMING:      {r.get('best_timing')}")
    print(f"WHY:         {r.get('timing_reason')}")
    print(f"USE CASE:    {r.get('use_case_tag')}")
    print(f"PERMISSION:  {r.get('edit_permission_note')}")

    _section("ASK EMAIL", r.get("ask_email", ""))
    _section("FOLLOW-UP 1 (5-7 days later)", r.get("follow_up_1", ""))
    _section("FOLLOW-UP 2 (7-10 days after #1)", r.get("follow_up_2", ""))

    qs = r.get("questions_to_make_it_easy") or []
    if qs:
        _section("OPTIONAL GUIDED QUESTIONS", "\n".join(f"  - {q}" for q in qs))
    print()


def main() -> None:
    print("=== Testimonial Collector Agent ===")
    print("Powered by free OpenRouter models. Costs $0 to test.\n")

    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        ctx = sys.stdin.read().strip()
        if not ctx:
            print("No input provided. Exiting.")
            return
    else:
        ctx = _read_block(
            "Describe the buyer (product they bought, where they are in the journey, "
            "any specific result or engagement you've noticed)"
        )
        if not ctx:
            print("No buyer context given. Exiting.")
            return

    print("\nThinking...")
    _print_result(make_ask(ctx))


if __name__ == "__main__":
    main()