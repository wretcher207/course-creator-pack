"""Lesson Outliner Agent — topic + audience + duration to video outline."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.client import chat, extract_json

PROMPT_FILE = Path(__file__).parent / "system_prompt.md"


def outline(brief: str) -> dict:
    system_prompt = PROMPT_FILE.read_text(encoding="utf-8")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"LESSON BRIEF:\n\n{brief}"},
    ]
    raw = chat(messages, max_tokens=2200, temperature=0.55)
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
    print>()
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
    print(f"LESSON:    {r.get('lesson_summary')}")
    print(f"BIG IDEA:  {r.get('single_big_idea')}")

    pre = r.get("prerequisites_check") or []
    if pre:
        _section("PREREQUISITES", "\n".join(f"  - {p}" for p in pre))

    _section("HOOK (read on camera)", r.get("hook", ""))
    _section("PROMISE", r.get("promise", ""))

    print()
    print("=" * 60)
    print("OUTLINE")
    print("=" * 60)
    for sec in r.get("outline", []):
        print()
        print(f"--- [{sec.get('approx_minutes')} min] {sec.get('section')} ---")
        for tp in sec.get("talking_points", []):
            print(f"  - {tp}")
        demo = sec.get("demo_or_visual", "").strip()
        if demo:
            print(f"  Visual: {demo}")

    _section("EXERCISE", r.get("exercise", ""))
    _section("CALLBACK + NEXT", r.get("callback_and_next", ""))

    cm = r.get("common_mistakes_to_address") or []
    if cm:
        _section("COMMON MISTAKES TO PRE-EMPT", "\n".join(f"  - {m}" for m in cm))

    sc = r.get("scope_creep_warnings") or []
    if sc:
        _section("[!] SCOPE CREEP — do NOT cover in this lesson", "\n".join(f"  - {s}" for s in sc))
    print()


def main() -> None:
    print("=== Lesson Outliner Agent ===")
    print("Powered by free OpenRouter models. Costs $0 to test.\n")

    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        brief = sys.stdin.read().strip()
        if not brief:
            print("No brief given. Exiting.")
            return
    else:
        brief = _read_block(
            "Describe the lesson (topic, audience, target length in minutes, "
            "what the previous/next lessons cover, anything explicitly NOT in scope)"
        )
        if not brief:
            print("No brief given. Exiting.")
            return

    print("\nThinking...")
    _print_result(outline(brief))


if __name__ == "__main__":
    main()