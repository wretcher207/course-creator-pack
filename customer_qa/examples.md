# Customer Q&A — Examples

## Example 1: "Is this for beginners?"

**Question:** "Hey is this course OK if I'm completely new to Python?"

**Product context:** "Advanced async Python course. Assumes 1+ year of Python experience. $147."

**Output:**
- fit_assessment: clear_not_fit
- draft_reply: answers honestly that it assumes 1+ year, points them at "Python Basics" course if creator has one
- honest_no_fit_reply: same, slightly shorter, even more direct
- common_pattern: "common — add to FAQ as 'level required'"

## Example 2: "Does this cover X feature?"

**Question:** "Does the course cover Stripe webhooks?"

**Product context:** "SaaS billing course covering Stripe Checkout, subscriptions, invoicing, dunning. Webhooks covered in module 4. $297."

**Output:**
- fit_assessment: clear_fit
- draft_reply: yes, module 4, here's the specific lesson title

## Example 3: Pricing pushback disguised as a question

**Question:** "Why is this $497 when there's a free YouTube series on the same topic?"

**Output:**
- question_intent: "the price is the real concern; the YouTube comparison is the framing"
- fit_assessment: unclear (depends on creator's positioning)
- draft_reply: addresses the comparison directly without trashing YouTube, names what the paid version adds (curation, sequence, accountability, support)
- common_pattern: "objection — consider adding to sales page above the price"

## Example 4: Vague "is this for me"

**Question:** "I'm an SDR thinking about going indie, would this help me?"

**Product context:** "Course on building a 1-person SaaS, assumes you can ship a web app. $397."

**Output:**
- fit_assessment: unclear
- follow_up_question: "Have you shipped a web app before? The course assumes you can build the product, not just sell it."
- draft_reply: asks the follow-up, doesn't push the buy

## Example 5: Refund window question

**Question:** "What's the refund policy if I get in and it's not what I expected?"

**Product context:** "30-day refund, no questions asked, refund button in the buyer dashboard."

**Output:**
- fit_assessment: clear_fit (this is a confidence question, not a doubt)
- draft_reply: states the policy plainly, names the self-serve refund button, no fine print
- common_pattern: "common — make sure refund policy is on the sales page above the buy button"
