# Testimonial Collector — Examples

## Example 1: Just-purchased

**Input:** "Maria bought the SaaS Billing course 30 minutes ago. She's brand new."

**Output:**
- best_timing: wait_until_finished
- timing_reason: "no result yet — testimonial would be empty calories"
- ask_email is still drafted but timing is flagged
- use_case_tag: do_not_use_yet

## Example 2: Mid-product, visible engagement

**Input:** "Devon completed modules 1-3, replied to my welcome email, mentioned he's setting up Stripe webhooks tonight."

**Output:**
- best_timing: ask_after_specific_milestone (after the webhook setup is live)
- ask_email opens with reference to the webhook setup
- questions_to_make_it_easy includes "what's working in production now that wasn't before?"

## Example 3: Completed + named result

**Input:** "Anya finished the course 2 weeks ago, posted on Twitter that her recovery rate jumped from 18% to 41%."

**Output:**
- best_timing: ask_now
- ask_email opens with that specific tweet's stat
- use_case_tag: sales_page (this is a banger quote-in-progress)
- edit_permission_note: asks for permission to use name + role + the stat she posted publicly

## Example 4: 6-months-later sphere

**Input:** "Tom bought 6 months ago. Hasn't replied to any nurture emails. Bought again last week — different product."

**Output:**
- best_timing: ask_now (the second purchase is the signal)
- ask_email leads with thanks for the second buy, asks about the first product's outcome
- use_case_tag: case_study (long-term retention story)

## Example 5: Refund-adjacent buyer

**Input:** "Karen replied to module 2 saying it's not what she expected, hasn't asked for a refund yet."

**Output:**
- best_timing: do_not_ask
- timing_reason: "fix the product fit first; testimonial ask now would feel tone-deaf"
- ask_email is not generated (or generated but flagged hard)
- questions_to_make_it_easy is replaced by a "what would have made this fit better?" — a different conversation
