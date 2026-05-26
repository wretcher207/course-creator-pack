# Course Creator Pack — Product Hunt Launch Guide

Everything you need to ship a listing that gets found, clicked, and upvoted.

---

## Before You Post

### 1. Set up your GitHub repo (DONE)
Repo is initialized at `C:\Users\david\workspace\course-creator-pack`
Public README is in place. Add a short description + topics on GitHub itself.

### 2. Make your repo "maker-ready"
Add these to the repo:
- **`DEMO_VIDEO_SCRIPT.md`** — the demo script (provided below)
- **`PRODUCT_HUNT_LAUNCH.md`** — this guide (so you remember your own plan)
- A `screenshots/` folder — at minimum, one animated GIF of the flow

To add the demo launcher: copy `run_demo.bat` from this folder to the repo root.

---

## The Product Hunt Listing

### When to post
**Tuesday, Wednesday, or Thursday.** Avoid Mondays (low traffic) and Fridays (weekend lag). Post at **6am Pacific** — that puts it at 9am Eastern when the US maker/creator audience is starting their day, and it stays on the front page through the morning wave.

### The 3 elements that make or break the listing

#### 1. Thumbnail (160×160 — this is your first impression)
- Use the existing `dist/cover.png` as a base
- Make it readable at tiny size: product name + one core value prop
- No small text, no fine detail
- Dark background + one bold accent color works on PH's white bg

#### 2. Tagline (max 20 words — appears in search and cards)
> "Seven AI agents for course creators. No SaaS. No monthly fee. $0 to run forever."

#### 3. Description (the full pitch)
Use the go-to-market copy from `dist/go-to-market.md` — section "Listing copy (paste into Gumroad description field)." That's already written for exactly this purpose.

### The sections to fill on PH

| Section | What to write |
|---|---|
| **Tagline** | "Seven AI agents for course creators. No SaaS. No monthly fee. $0 to run forever." |
| **Description** | Paste the full Gumroad description from `dist/go-to-market.md` |
| **Gallery** | cover.png, a screenshot of one agent output (email sequence JSON), screenshot of the bat file list |
| **Video** | Link to demo video on YouTube/Vimeo (see script below) |
| **Links** | Gumroad purchase link + GitHub repo |
| **Topics** | `ai`, `productivity`, `no-code-tools`, `copywriting`, `email-marketing`, `course-creator` |

---

## The Demo Video

Length: **90 seconds maximum.** The first 15 seconds are the hook.

See `DEMO_VIDEO_SCRIPT.md` for the full shot-by-shot script.

**Recording tips:**
- Use OBS (free) or Loom — either works
- Record at 1080p, export at 1080p
- Show your actual screen, not a slide deck
- Go slow. Read the prompts out loud. PAUSE after showing output.

**TL;DR structure:**
1. Show the folder (5s) — "Here's what you get."
2. Run one agent live (60s) — Launch Email Sequencer, paste a 2-line brief, show output
3. Show the output in the console (20s) — "This is what you'd have paid a copywriter $2k for"
4. Close (5s) — "Buy once, own forever. Link below."

---

## Pre-Launch (48 hours before)

### Build early traction
1. **Post on X/Twitter 48h before** with the PH link:
   > "Launching on Product Hunt tomorrow at 6am Pacific. Course Creator Pack — 7 AI agents, $0/month to run. [link]"

2. **Email your existing list** (the one from the go-to-market doc):
   > "I'm launching on PH tomorrow. If this is useful to you, an upvote helps me reach more creators like you. [link]"

3. **DM 5-10 people** who are in your niche and have posted on PH before. Ask them to upvote when it's live. Don't ask for a review — just an upvote.

### The PH algorithm
PH surfaces products that get early upvotes in the first 2-3 hours. **10-15 upvotes in the first 2 hours** is the threshold for hitting the trending queue. Build that initial wave before posting.

---

## The Day-Of Sequence

### 6am Pacific: Post goes live
- Post the PH link to X/Twitter
- Post to LinkedIn
- Email your list
- DM your contacts who said they'd help

### First 2 hours: Comment on every upvote
PH shows new comments in the activity feed — each one is a visibility event. For every upvote notification, post a brief comment thanking them and adding a detail.

**Comment template:**
> "Thanks! This is the [X] agent — happy to answer any questions about how it works."

### Mid-day: Second wave
If you've hit 20+ upvotes and are trending, post again:
> "We're #3 on PH right now — thank you. [one-line value prop] [link]"

### Keep the launch alive 48h
Keep commenting, keep responding to questions. A listing with active maker conversation stays visible longer.

---

## Product Hunt FAQ

**Q: Do I need to be verified on PH to post?**
A: No. Create a maker profile, verify your email. That's it.

**Q: Can I post on behalf of a company?**
A: Yes. You can post as yourself or create a "Company" page. Posting as yourself with a company link is fine for a one-person product.

**Q: I have a Gumroad product. Can I link directly to it?**
A: Yes. You can put your Gumroad purchase link in "Links" and your GitHub in the description.

**Q: What if I don't get upvotes in the first 2 hours?**
A: It's not over. Low-traffic days (Friday-Sunday) are actually easier to get #1 on the homepage even with fewer total upvotes. Post again in 2 weeks if this one doesn't trend.

**Q: Should I offer a discount to PH visitors?**
A: Yes — and put it in the description. "Launch price: $39 (normally $49)" is a strong conversion signal.

---

## Quick Checklist

- [ ] GitHub repo is public and has a README
- [ ] `DEMO_VIDEO_SCRIPT.md` is in the repo
- [ ] Demo video is recorded and uploaded (90s or less)
- [ ] `dist/cover.png` is clean and readable as a thumbnail
- [ ] Product Hunt maker account is verified
- [ ] Listing copy is pasted from `dist/go-to-market.md`
- [ ] Pre-launch X post is drafted (not sent yet)
- [ ] Email to list is drafted (not sent yet)
- [ ] 10 people have been DM'd to be ready to upvote
- [ ] Launch time is set: 6am Pacific, Tuesday–Thursday

---

## The One-Click Demo

The file `run_demo.bat` in this folder is your demo launcher. Run it to show the full flow in a console window — paste input, see output. Works on any Windows machine with Python 3.11+.

Copy `run_demo.bat` to the repo root so makers can see it when they land on GitHub.