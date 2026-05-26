# Course Creator Pack — Go-to-Market

For David's eyes. Internal launch playbook.

## Product positioning

**Promise:** "Seven AI agents that take the writing, customer support, and launch busywork off a course creator's plate. Costs $0/month to run."

**Anti-positioning** (what it's NOT):
- Not a course platform
- Not an ESP
- Not a payment processor
- Not a SaaS subscription

**Buyer persona:** working course creator / info-product seller / paid newsletter operator. Ships 1-3 launches/year. Audience 1k-50k. Already on Gumroad / Lemon Squeezy / Stripe / their own site. Drowning in writing tasks during launch week. Wants to own the tool.

---

## Pricing

| Tier | Price | When |
|---|---|---|
| Launch | **$39** | First 14 days |
| Normal | **$49** | After launch |
| Bundle (with v1 + v2) | **$79** | Anytime |

**Why $39 launch:** matches realtor pack price point. Same engine, same format, same positioning.

**Bundle math:** v1 ($19) + v2 realtor ($49) + v3 course ($49) = $117 anchor. $79 bundle = "save $38" — strong upsell to existing buyers.

---

## Listing copy (paste into Gumroad description field)

```
Seven AI agents built for one job: take the writing, customer support, and launch busywork off a working course creator's plate.

What's inside:

• Launch Email Sequencer — product + audience + dates → 6-email launch sequence with subjects, timing, copy
• Sales Page Critique — paste your sales page → headline score, 3 rewrites, named issues, biggest lift, 10-min wins
• Refund De-escalator — refund request → real-reason read + tactful reply + fallback if they push back
• Customer Q&A — buyer's "is this for me?" + your product → honest answer + fit signal + no-fit reply
• Affiliate Outreach — terms + a single prospect → personalized pitch + follow-up + DM-length version
• Testimonial Collector — buyer context → right-timing call + ask + 2 follow-ups + guided questions
• Lesson Outliner — topic + audience + duration → hook script, single big idea, outline, applied exercise

Plus a 1-page Launch Week Playbook that shows you exactly when to run each one across a 7-day launch.

How it stays at $0:

Built on OpenRouter's free-tier models with a 7-model fallback chain. ~200 requests/day on free tier — enough for an entire launch week. If you outgrow it, swap to a paid model in one line.

What you actually get:

• Seven agents (Python, plain code, ~400 lines total)
• Every prompt in a markdown file you can edit
• One-click .bat launchers for Windows (no terminal commands, ever)
• setup.bat to install everything in 60 seconds
• 5 worked examples per agent
• Launch Week Playbook showing how to use the pack across one 7-day launch
• Smoke test that validates all 7 agents in 30 seconds

What you don't get:

• No SaaS subscription
• No login
• No course platform you have to migrate to
• No monthly fee
• No "credits" to top up

You buy this once. It's yours.

License: use the agents and their output commercially in your own creator business and in client work. Modify the code freely. Don't resell it.

Requires: Python 3.11+, free OpenRouter API key (no credit card needed), Windows 10/11.
```

### One-liner / summary for listing card (140 chars)
```
Seven AI agents that take the writing, customer support, and launch busywork off a course creator's plate. $0/month forever to run.
```

---

## Tags (Gumroad — Share tab, max 5)

```
course creators
info products
ai
agents
automation
```

---

## Cover image direction

- 1200x675 hero
- Top half: 4-3 grid of 7 agent name cards
- Bottom half: "$0 / MONTH FOREVER" + tagline
- Type: monospace headlines, sans-serif body
- Color: deep black + electric purple #7B5BFF (distinct from realtor pack's gold; reads as "creator economy / digital")
- DO NOT use: stock photo of person at laptop with coffee, light-mode dashboards, anything that looks like a SaaS landing page

`dist/make_cover.py` generates this.

---

## Launch posts

### LinkedIn (Day 1)

> I built seven AI agents for working course creators.
>
> Launch Email Sequencer. Sales Page Critique. Refund De-escalator. Customer Q&A. Affiliate Outreach. Testimonial Collector. Lesson Outliner.
>
> No SaaS. No platform migration. No monthly fee. Free OpenRouter tier means it costs $0/month to run.
>
> The whole pack is Python + markdown prompts you can read in 20 minutes. You buy it once and own it.
>
> $39 for the next two weeks. $49 after.
>
> Link in comments.

### X / Twitter (Day 1, evening)

> shipped: Course Creator Pack
>
> 7 AI agents for course creators + info-product sellers. launch email sequencer, sales page critique, refund de-escalator, customer Q&A, affiliate outreach, testimonial collector, lesson outliner.
>
> $0/month to run (free openrouter tier). $39 launch, $49 normal.
>
> [link]

### Email to existing v1 + v2 buyers (Day 1)

> Subject: V3 is out — bundle is $79 if you want all three
>
> Hey,
>
> If you bought the AI Agents Starter Kit or the Realtor Agent Pack, you saw the engine. V3 is the same engine pointed at course creators and info-product sellers.
>
> Seven new agents:
>
> * Launch Email Sequencer (the 6-email launch sequence in 5 minutes)
> * Sales Page Critique (specific edits, named issues, headline rewrites)
> * Refund De-escalator
> * Customer Q&A
> * Affiliate Outreach
> * Testimonial Collector
> * Lesson Outliner
>
> $39 standalone launch price ($49 normal). Bundle (v1 + v2 + v3) is $79 — save $38 vs buying separately.
>
> Reply if you want the bundle lane.

### Indie Hackers post (Day 2)

> Just shipped the third pack in my AI agents lineup — this one for course creators. Same engine, niche prompts. The play: $39 vertical packs, free OpenRouter tier so buyers pay nothing to run them, no SaaS to maintain.
>
> Three packs in: starter kit ($19), realtor pack ($39), course creator pack ($39). The engine + prompts pattern is the unlock — each new pack is ~1 day of focused prompt work + listing copy.
>
> If you sell info products and want to see the launch, link in profile.

---

## DPD (deadpixeldesign.com) listing

Same copy. Same price. Gumroad-link-out flavor first. Cover image goes at `dead-pixel-design-v4/public/workflows/course-creator-pack/`.

---

## Lemon Squeezy

Queue for week 3+. Same pricing.

---

## Targets

| Window | Sales target | Outcome trigger |
|---|---|---|
| Week 1 | 5 sales | proves second-vertical thesis |
| Week 4 | 20 sales | raise to $49, queue V4 |
| Month 3 | 50 sales | ship vertical pack #4 |

If under 5 sales in week 1: rewrite cover + headline before lowering price. Course creator audience is on Gumroad already — a slow launch likely means positioning, not pricing.

---

## V4 candidates (after this lands)

- **Local Service Biz Pack** — Lead Spider tie-in, contractors / HVAC / electricians
- **Property Manager Pack** — adjacent to realtor pack, cross-sell to v2 buyers
- **Indie Dev / SaaS Founder Pack** — overlaps v1 buyers, dev-Twitter channel
- **Bundle SKU** as its own listing on DPD (not just a Gumroad discount code)
