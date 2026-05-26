"""Affiliate Outreach Agent — prospect details to personalized pitch."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.client import chat, extract_json

PROMPT_FILE = Path(__file__).parent / "system_prompt.md"


def make_pitch(product_and_terms: str, prospect: str) -> dict:
    system_prompt = PROMPT_FILE.read_text(encoding="utf-8")
    user_msg = (
        f"PRODUCT + AFFILIATE TERMS:\n{product_and_terms}\n\n"
        f"PROSPECT:\n{prospect}"
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_msg},
    ]
    raw = chat(messages, max_tokens=1400, temperature=0.55)
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
    print(f"FIT:        {r.get('fit_assessment') or r.get('fit_read')}")
    print(f"FIT SCORE:  {r.get('fit_score')}/10")
    print(f"ANGLE:      {r.get('best_angle')}")

    _section(f"EMAIL — Subject: {r.get('subject_line', '')}", r.get("email_body", ""))
    _section("FOLLOW-UP (5-7 days later)", r.get("follow_up_email", ""))
    _section("DM / SMS VERSION", r.get("dm_short_version", ""))

    gaps = r.get("research_gaps") or []
    if gaps:
        _section("RESEARCH BEFORE SENDING", "\n".join(f"  - {g}" for g in gaps))
    dnp = r.get("do_not_pursue_signals") or []
    if dnp:
        _section("[!] DO-NOT-PURSUE SIGNALS", "\n".join(f"  - {s}" for s in dnp))
    print()


def main() -> None:
    print("=== Affiliate Outreach Agent ===")
    print("Powered by free OpenRouter models. Costs $0 to test.\n")

    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        content = sys.stdin.read().strip()
        parts = content.split("END\n")
        if len(parts) < 2:
            print("Invalid input format. Expected: product/terms block END, prospect block END")
            return
        pt = parts[0].strip()
        p = parts[1].strip()
        if not pt:
            print("No product/terms given. Exiting.")
            return
        if not p:
            print("No prospect given. Exiting.")
            return
    else:
        pt = _read_block(
            "Paste your product + affiliate terms (commission %, cookie window, payout, etc.)"
        )
        if not pt:
            print("No product/terms given. Exiting.")
            return
        print()
        p = _read_block(
            "Describe the prospect (their newsletter / podcast / YouTube / community, audience size, niche, recent work)"
        )
        if not p:
            print("No prospect given. Exiting.")
            return

    print("\nThinking...")
    _print_result(make_pitch(pt, p))


if __name__ == "__main__":
    main()
