"""Sales Page Critique Agent — paste a sales page, get specific edits."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.client import chat, extract_json

PROMPT_FILE = Path(__file__).parent / "system_prompt.md"


def critique(page_text: str, context: str = "") -> dict:
    system_prompt = PROMPT_FILE.read_text(encoding="utf-8")
    user_msg = (
        f"SALES PAGE:\n{page_text}\n\n"
        f"CONTEXT (optional):\n{context or '(none)'}"
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_msg},
    ]
    raw = chat(messages, max_tokens=2200, temperature=0.4)
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
    print(f"PAGE: {r.get('page_summary')}")
    print(f"HEADLINE SCORE: {r.get('headline_score')}/10")
    print(f"BIGGEST LIFT: {r.get('biggest_lift')}")
    print(f"SOCIAL PROOF: {r.get('social_proof_assessment')}")
    print(f"TONE MATCH:   {r.get('tone_match')}")
    print(f"CTA:          {r.get('cta_assessment')}")

    rewrites = r.get("headline_rewrites") or []
    if rewrites:
        _section("HEADLINE REWRITES", "\n".join(f"  - {h}" for h in rewrites))

    issues = r.get("clarity_issues") or []
    if issues:
        out = []
        for i in issues:
            out.append(f"  [{i.get('where', '?')}]")
            out.append(f"     Issue: {i.get('issue', '')}")
            out.append(f"     Fix:   {i.get('fix', '')}")
            out.append("")
        _section("CLARITY ISSUES", "\n".join(out))

    gaps = r.get("objection_gaps") or []
    if gaps:
        out = []
        for g in gaps:
            out.append(f"  Objection: {g.get('objection', '')}")
            out.append(f"     Where:    {g.get('where_to_address', '')}")
            out.append(f"     Suggest:  {g.get('suggested_copy', '')}")
            out.append("")
        _section("OBJECTION GAPS", "\n".join(out))

    sp = r.get("social_proof_suggestions") or []
    if sp:
        _section("SOCIAL PROOF SUGGESTIONS", "\n".join(f"  - {s}" for s in sp))

    cta = r.get("cta_rewrites") or []
    if cta:
        _section("CTA REWRITES", "\n".join(f"  - {c}" for c in cta))

    wins = r.get("small_wins") or []
    if wins:
        _section("SMALL WINS (10-min edits)", "\n".join(f"  - {w}" for w in wins))
    print()


def main() -> None:
    print("=== Sales Page Critique Agent ===")
    print("Powered by free OpenRouter models. Costs $0 to test.\n")

    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        page = sys.stdin.read().strip()
        if not page:
            print("No input provided. Exiting.")
            return
        ctx = ""
    else:
        page = _read_block("Paste the full sales page (headline + body + FAQ + CTA + price)")
        if not page:
            print("No page given. Exiting.")
            return
        print()
        ctx = _read_block(
            "Optional context (target buyer, current conversion rate, price) — or just type END"
        )

    print("\nThinking...")
    _print_result(critique(page, ctx))


if __name__ == "__main__":
    main()
