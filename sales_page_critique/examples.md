# Sales Page Critique — Examples

## Example 1: Vague headline + missing objection

**Input:** Sales page for "ProductivityOS" with headline "The complete system for getting things done" and no answer to "how is this different from Notion templates I can buy for $19."

**Output highlights:**
- headline_score: 4 (names the product but not the transformation)
- headline_rewrites: 3 versions that lead with the transformation
- objection_gaps: includes the Notion-template question with suggested copy for the FAQ
- biggest_lift: "rewrite the headline"

## Example 2: Strong page, only small wins

**Input:** Polished sales page with specific transformation, named testimonials, single CTA, addressed-price-objection block.

**Output highlights:**
- headline_score: 8
- clarity_issues: empty array
- objection_gaps: empty array
- social_proof_assessment: strong
- biggest_lift: "split the testimonial section so one is above the price, not all bunched at bottom"
- small_wins: 3 actual small edits

## Example 3: Tone mismatch

**Input:** Course for plumbers, page written in tech-bro voice ("Stop hustling, start shipping").

**Output highlights:**
- tone_match: "The tech-bro framing won't land with a plumber audience — they ship every day"
- biggest_lift: "rewrite all the body copy in language a working plumber actually speaks"
- headline_rewrites: 3 in plumber voice

## Example 4: Generic social proof

**Input:** Page has 5-star icon + "trusted by thousands" — no real names, no real quotes.

**Output highlights:**
- social_proof_assessment: generic
- social_proof_suggestions: replace with 2-3 real quotes + name + role + outcome
- objection_gaps: includes "How do I know anyone has actually finished this?"

## Example 5: B2B premium page, $4,800 ticket

**Input:** Page selling a $4,800 agency operator program.

**Output highlights:**
- cta_assessment: "Single CTA is right for this price point but 'Buy Now' is too low-friction — book-a-call would feel more aligned"
- cta_rewrites: 2 alternatives that match premium positioning
- objection_gaps: includes the "I can hire a coach for this" objection with suggested handling
