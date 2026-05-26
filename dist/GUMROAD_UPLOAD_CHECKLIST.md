# Gumroad Upload Checklist — Course Creator Pack

Composio's Gumroad API is read-only (no `CREATE_PRODUCT`), so this is a manual UI flow. ~10 minutes.

## Files to upload

| File | Purpose | Path |
|---|---|---|
| `course-creator-pack.zip` | The product file buyers download | `dist/course-creator-pack.zip` |
| `cover.png` | Listing cover image (1200x675) | `dist/cover.png` |

Before upload, run:

```powershell
.\dist\build_zip.ps1
```

That rebuilds the Gumroad zip and includes `Launch Email Sequencer.exe` plus `START-HERE.txt`.

## Step-by-step

### 1. Create the product
- Gumroad → Products → New product
- Type: **Digital product**
- Name: **Course Creator Pack**
- Price: **$39** (launch — first 14 days)
- Click Next

### 2. Upload the file + cover
- Drag `course-creator-pack.zip` into the file uploader
- Upload `cover.png` as the cover

### 3. Description
Paste the full description from `dist/go-to-market.md` (the "Listing copy" section, the block inside the triple backticks).

### 4. Summary line (under product name)
```
Seven AI agents that take the writing, customer support, and launch busywork off a course creator's plate. $0/month forever to run.
```

### 5. SAVE — at this point you have a draft

### 6. Tags — Share tab, NOT Product tab (gotcha)
- course creators
- info products
- ai
- agents
- automation

### 7. Settings checklist
- [ ] **Receipt note:** "Thanks. For the launch email flow, double-click Launch Email Sequencer.exe. For the full 7-agent pack, run setup.bat first, then any of the run_*.bat files. Open launch_week_playbook.md to see how to use the pack across a launch."
- [ ] **Refund policy:** 30-day money back
- [ ] **Pay what you want:** OFF
- [ ] **Quantity:** Single download

### 8. Pricing schedule
- Today → Day 14: **$39**
- Day 15+: bump to **$49**
- Bundle discount code (v1 + v2 + v3 → $79): create a Gumroad discount code valid only when buyer has all three in cart, OR list the bundle as its own SKU on DPD

### 9. Publish + share
- Click Publish
- Copy the public URL (slug will look like `/l/xxxxxx`)
- Update `src/content/workflows/course-creator-pack.md` body links to use the real slug
- Cross-post — see `dist/go-to-market.md` for LinkedIn / X / IH posts and the v1+v2-buyer email

### 10. Optional: webhook for sales notifications
Composio supports `GUMROAD_SUBSCRIBE_TO_RESOURCE` for the `sale` event. Skip unless you want push notifications.

## After-launch

- [ ] Email me the real Gumroad slug — I'll update the DPD listing PR and merge
- [ ] Mirror to deadpixeldesign.com (use `dead-pixel-design-publish` skill, same pattern as realtor pack)
- [ ] Queue for Lemon Squeezy in week 3
- [ ] First sales target: 5 in week 1
- [ ] Email v1 + v2 buyers about the bundle
