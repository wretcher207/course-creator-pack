"""Launch Email Sequencer — product + audience to 6-email launch sequence."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.client import chat, extract_json

PROMPT_FILE = Path(__file__).parent / "system_prompt.md"


def build_sequence(launch_context: str) -> dict:
    system_prompt = PROMPT_FILE.read_text(encoding="utf-8")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"LAUNCH CONTEXT:\n\n{launch_context}"},
    ]
    raw = chat(messages, max_tokens=2800, temperature=0.6)
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


def _print_result(r: dict) -> None:
    if "_error" in r:
        print("\n[!] Model output was not parseable JSON:")
        print(r["_error"])
        print("\nRaw output:")
        print(r["_raw"])
        return

    print()
    print("=" * 60)
    print(f"LAUNCH:   {r.get('launch_summary')}")
    print(f"STRATEGY: {r.get('sequence_strategy')}")
    print("=" * 60)

    for e in r.get("emails", []):
        print()
        print(
            f"--- Email #{e.get('email_number')} | {e.get('send_when')} | {e.get('purpose')} ---"
        )
        print(f"Subject:  {e.get('subject_line', '')}")
        print(f"Preview:  {e.get('preview_text', '')}")
        print()
        print(e.get("body", ""))
        print()
        print(f"CTA: {e.get('cta', '')}")

    print()
    print("-" * 60)
    print(f"Abandonment followup: {r.get('abandonment_followup', '')}")
    print(f"Post-close recap:     {r.get('post_close_recap', '')}")
    print()


def main() -> None:
    print("=== Launch Email Sequencer ===")
    print("Powered by free OpenRouter models. Costs $0 to test.\n")

    ctx = _read_block(
        "Describe the launch (product, who it is for, transformation, price, "
        "launch dates, bonuses if any, list size, voice notes)"
    )
    if not ctx:
        print("No launch context given. Exiting.")
        return

    print("\nThinking...")
    _print_result(build_sequence(ctx))


if __name__ == "__main__":
    main()
