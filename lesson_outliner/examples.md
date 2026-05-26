# Lesson Outliner — Examples

## Example 1: SaaS billing — Stripe webhook setup

**Input:** "Topic: setting up Stripe webhooks for subscription events. Audience: indie SaaS founders, can ship a Node app. Length: 12 min. Previous lesson: Stripe Checkout. Next: handling failed payments. NOT in scope: webhook signature verification (next module)."

**Output highlights:**
- single_big_idea: "wire one webhook endpoint that responds to subscription.created"
- outline has 5 sections summing to 12 min
- scope_creep_warnings: ["signature verification — flagged in next module"]
- exercise: "set up the endpoint, hit it with the Stripe CLI, paste the resulting log line"

## Example 2: Yoga teacher training — sequencing

**Input:** "Topic: how to sequence a 60-min flow. Audience: brand new teachers. Length: 18 min."

**Output highlights:**
- single_big_idea: "build a flow with peak-pose backwards-design"
- outline includes a "common mistake" section (most new teachers front-load the hardest poses)
- exercise: "design a 60-min sequence from a single peak pose, send it in"

## Example 3: Brief is too big for the time

**Input:** "Topic: marketing your course. Length: 8 min."

**Output highlights:**
- scope_creep_warnings: ["this is 4-6 lessons, not one — pick ONE channel or ONE phase to teach in 8 min"]
- single_big_idea hedges and asks the creator to narrow the brief
- outline is shorter and shallower because the brief is too broad

## Example 4: Highly technical, short lesson

**Input:** "Topic: writing your first React custom hook. Audience: developers comfortable with React. Length: 6 min. Next lesson: testing custom hooks."

**Output highlights:**
- prerequisites_check: ["comfort with useState and useEffect"]
- outline is tight (4 sections)
- exercise: "extract one piece of stateful logic from a real component into a custom hook"
- demo_or_visual specifies "split screen: editor on left, browser on right"

## Example 5: Soft skill lesson

**Input:** "Topic: handling negative reviews on your launch day. Audience: course creators about to launch. Length: 10 min."

**Output highlights:**
- single_big_idea: "respond once, professionally, then move on"
- outline includes "Why your urge to argue is wrong" as a section
- exercise: "draft a response to the worst hypothetical review and walk away from it for 2 hours before sending"
- common_mistakes_to_address includes "responding within 60 minutes" and "going line-by-line"
