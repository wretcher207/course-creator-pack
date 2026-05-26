# Refund De-escalator — Examples

## Example 1: Buyer remorse the next day

**Input:** "Hey, I bought your course last night and I'm thinking I might have jumped the gun, can I get a refund?"

**Context:** "$197 course, 14-day refund policy, day 1 since purchase."

**Output:**
- real_reason: classic buyer remorse from making the decision after-hours
- recommendation: refund_clean
- draft_reply: warm, no shame, refund processed without conditions
- internal_note: "single buyer-remorse refund within 24h, normal pattern, no concern"

## Example 2: Implicit "I didn't watch it"

**Input:** "I tried but the course just isn't what I needed. Refund please."

**Output:**
- real_reason: likely never opened module 1 — vague language is the tell
- recommendation: retain_with_swap (offer a 15-min 1:1 to figure out what they actually need)
- if_they_push_back: clean refund
- internal_note: "if you see this pattern recurring, the welcome email may not be setting buyers up to start"

## Example 3: Angry, threatens chargeback

**Input:** "this is a complete scam, I'm filing a chargeback if you don't refund me TODAY"

**Output:**
- buyer_state: scammed_feeling
- recommendation: refund_clean
- recommendation_reason: a chargeback costs more than the refund — defuse and document
- draft_reply: brief, calm, no argument, processes refund
- policy_flags: ["chargeback threat — process refund within 24h regardless of policy", "save the original purchase email for records"]

## Example 4: Outside policy

**Input:** "I bought the course 6 months ago and just got around to it. Doesn't apply to my business. Refund?"

**Context:** "30-day refund policy."

**Output:**
- recommendation: decline_outside_policy
- draft_reply: warm but firm — references the policy by name without quoting it like a contract, offers a swap into a different product OR a partial credit
- if_they_push_back: holds the line, offers nothing more
- internal_note: log refund-attempts at 6mo, this is a pattern worth tracking

## Example 5: Embarrassed, "this is too advanced"

**Input:** "I'm not at the level for this, sorry, I was hoping it'd start more from scratch."

**Output:**
- buyer_state: embarrassed
- recommendation: retain_with_swap (if you have a beginner product) OR refund_clean (if not)
- draft_reply: warm, removes shame, names the issue without restating their words back at them
- internal_note: "if you see this 3+ times, your sales page is over-promising the level"
