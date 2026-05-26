# Course Creator Pack
> Seven AI agents that take the writing, customer support, and launch busywork off a working course creator's plate. Runs forever at $0/month.

[Course Creator Pack · Gumroad](https://DAVID'S_GUMROAD_LINK)

## What this is

Seven production-grade AI agents built for course creators and info-product sellers. Each one replaces a specific freelance hire or agency deliverable — and they run on a free OpenRouter API key, so they cost $0/month forever.

| Agent | What it does | Replaces |
|---|---|---|
| **Launch Email Sequencer** | Product + audience + dates → 6-email launch sequence with subjects, timing, copy | Email copywriter, $1.5k–3k/launch |
| **Sales Page Critique** | Paste your sales page → specific edits, headline rewrites, named issues, biggest lift call | Conversion copywriter, $500–2k audit |
| **Refund De-escalator** | Refund request → real reason read + tactful reply + fallback | CS retainer, $500–1.5k/month |
| **Customer Q&A** | Buyer's question + your product → honest answer + fit signal + no-fit reply | Pre-sales support, ~10 min/question |
| **Affiliate Outreach** | Terms + prospect → personalized pitch, follow-up, DM version | Affiliate manager, $1k–3k/month |
| **Testimonial Collector** | Buyer context → right-timing call, ask email, 2 follow-ups, guided questions | CS coordinator, ~30 min/ask |
| **Lesson Outliner** | Topic + audience + duration → hook, single big idea, sectioned outline, exercise | Curriculum designer, $300–800/lesson |

## 60-second setup

```
1. Install Python 3.11+ (https://python.org/downloads — check "Add to PATH")
2. Get a free API key at https://openrouter.ai/keys (no credit card)
3. Save the key to your Desktop as openrouter-api.txt
4. Double-click setup.bat
5. Done.
```

## Run any agent

| Double-click | What happens |
|---|---|
| `run_launch_email_sequencer.bat` | Get a 6-email launch sequence |
| `run_sales_page_critique.bat` | Get specific edits + rewrites for your sales page |
| `run_refund_deescalator.bat` | Get a tactful reply to any refund request |
| `run_customer_qa.bat` | Get an honest answer + no-fit reply for buyers |
| `run_affiliate_outreach.bat` | Get a personalized pitch + follow-up for an affiliate |
| `run_testimonial_collector.bat` | Get the right ask email and follow-ups |
| `run_lesson_outliner.bat` | Get a structured lesson outline with hook + exercise |

## How it stays at $0/month

The shared client ships with a **7-model fallback chain** on OpenRouter's free tier. If the first model rate-limits, the next one picks up silently. That's ~200 requests/day — enough for an entire launch week. If you outgrow it: one line to add a paid model.

## Project structure

```
course-creator-pack/
  shared/
    client.py          # OpenRouter chat + fallback chain
    keyloader.py       # Key from file or env var
  launch_email_sequencer/
    agent.py           # Agent logic
    system_prompt.md  # The prompt — edit freely
    examples.md        # 5 sample inputs/outputs
  sales_page_critique/ (same structure)
  refund_deescalator/ (same structure)
  customer_qa/         (same structure)
  affiliate_outreach/  (same structure)
  testimonial_collector/ (same structure)
  lesson_outliner/     (same structure)
  run_*.bat            # One launcher per agent
  setup.bat            # One-time install
  examples/            # Screenshots + sample output
```

## Customization

**Edit an agent's behavior:** Open `agent/system_prompt.md`. It's plain markdown — the agent reads it on every run. Changes take effect immediately, no code.

**Swap models:** Edit `FREE_MODELS` in `shared/client.py`.

**Use a paid model:** Change `model=` in `chat()` to `anthropic/claude-sonnet` or any OpenRouter model.

## License

See `LICENSE.md`. TL;DR: use it commercially in your own creator business. Modify prompts and code freely. Don't resell it.

---

*Want to see when to run each agent across a real launch week? See `dist/launch_week_playbook.md`.*
