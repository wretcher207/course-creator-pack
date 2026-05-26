"""End-to-end smoke test for all 7 agents.

Runs each agent with a small canned input and prints PASS/FAIL.
Hits the real OpenRouter API. Will use ~7 requests against your free quota.

Usage (from repo root, after setup.bat):
    venv\\Scripts\\python.exe smoke_test.py
"""
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


REQUIRED_FIELDS = {
    "launch_email_sequencer": ["launch_summary", "sequence_strategy", "emails",
                               "abandonment_followup", "post_close_recap"],
    "sales_page_critique": ["page_summary", "headline_score", "headline_rewrites",
                            "clarity_issues", "objection_gaps", "biggest_lift", "small_wins"],
    "refund_deescalator": ["real_reason", "buyer_state", "recommendation",
                           "draft_reply", "if_they_push_back", "internal_note"],
    "customer_qa": ["question_intent", "fit_assessment", "fit_reason",
                    "draft_reply", "honest_no_fit_reply"],
    "affiliate_outreach": ["fit_read", "fit_score", "best_angle", "subject_line",
                           "email_body", "follow_up_email", "dm_short_version", "research_gaps"],
    "testimonial_collector": ["buyer_stage_read", "best_timing", "ask_email",
                              "follow_up_1", "follow_up_2", "questions_to_make_it_easy", "use_case_tag"],
    "lesson_outliner": ["lesson_summary", "single_big_idea", "hook", "promise",
                        "outline", "exercise", "callback_and_next"],
}


def _check(name: str, result: dict) -> tuple[bool, str]:
    if "_error" in result:
        return False, f"model returned non-JSON: {result.get('_error')}"
    missing = [f for f in REQUIRED_FIELDS[name] if f not in result]
    if missing:
        return False, f"missing fields: {missing}"
    if name == "launch_email_sequencer":
        emails = result.get("emails", [])
        if len(emails) != 6:
            return False, f"expected 6 emails, got {len(emails)}"
    if name == "lesson_outliner":
        outline = result.get("outline", [])
        if len(outline) < 4 or len(outline) > 7:
            return False, f"expected 4-7 outline sections, got {len(outline)}"
    return True, "ok"


def run() -> int:
    failures = 0

    cases: list[tuple[str, callable]] = []

    from launch_email_sequencer.agent import build_sequence
    cases.append((
        "launch_email_sequencer",
        lambda: build_sequence(
            "$197 6-week productivity course for solo SaaS founders. List 4,200 indie devs. "
            "Cart opens Mon, closes Fri midnight. Bonus: 1:1 review for first 20. "
            "Voice: direct, technical, no fluff."
        ),
    ))

    from sales_page_critique.agent import critique
    cases.append((
        "sales_page_critique",
        lambda: critique(
            "Headline: ProductivityOS. Subhead: The complete system for getting things done. "
            "Body: ProductivityOS gives you everything you need. Modules cover tasks, calendar, "
            "habits, and reviews. CTA: Buy Now $97. Refund: 30 days.",
            "Audience: indie devs and solo founders. Current conversion ~1.2%."
        ),
    ))

    from refund_deescalator.agent import respond
    cases.append((
        "refund_deescalator",
        lambda: respond(
            "Hey, I bought your course last night and I'm thinking I jumped the gun, can I get a refund?",
            "$197 course, 14-day refund policy, day 1 since purchase."
        ),
    ))

    from customer_qa.agent import answer
    cases.append((
        "customer_qa",
        lambda: answer(
            "Hey is this course OK if I'm completely new to Python?",
            "Advanced async Python course. Assumes 1+ year of Python experience. "
            "Covers asyncio, trio, FastAPI patterns. $147."
        ),
    ))

    from affiliate_outreach.agent import make_pitch
    cases.append((
        "affiliate_outreach",
        lambda: make_pitch(
            "$197 SaaS billing course. 30% commission, 60-day cookie, $59 avg payout.",
            "Maria runs the 'Indie Stripe' newsletter, 18k subs, weekly issue, mostly indie SaaS founders. "
            "Last issue covered Stripe webhook signature verification."
        ),
    ))

    from testimonial_collector.agent import make_ask
    cases.append((
        "testimonial_collector",
        lambda: make_ask(
            "Anya finished the SaaS Billing course 2 weeks ago. Posted on Twitter that her "
            "recovery rate jumped from 18% to 41% after applying module 3."
        ),
    ))

    from lesson_outliner.agent import outline
    cases.append((
        "lesson_outliner",
        lambda: outline(
            "Topic: setting up Stripe webhooks for subscription events. "
            "Audience: indie SaaS founders, can ship a Node app. Length: 12 min. "
            "Previous lesson: Stripe Checkout. Next: handling failed payments. "
            "NOT in scope: webhook signature verification (covered next module)."
        ),
    ))

    for name, fn in cases:
        print(f"[{name}] running...", flush=True)
        try:
            result = fn()
            ok, msg = _check(name, result)
            if ok:
                print(f"[{name}] PASS")
            else:
                print(f"[{name}] FAIL — {msg}")
                failures += 1
        except Exception as e:
            print(f"[{name}] FAIL — exception: {e}")
            traceback.print_exc()
            failures += 1

    print()
    print("=" * 60)
    if failures == 0:
        print(f"All {len(cases)} agents passed.")
        return 0
    print(f"{failures} of {len(cases)} agents failed.")
    return 1


if __name__ == "__main__":
    sys.exit(run())
