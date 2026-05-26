@echo off
chcp 65001 >nul 2>&1
title Course Creator Pack — Live Demo
color 0A
mode con cols=100 lines=40

echo.
echo  =============================================================
echo   COURSE CREATOR PACK — LIVE DEMO
echo   Running the Launch Email Sequencer with a real example
echo  =============================================================
echo.
echo  This demo runs the Launch Email Sequencer agent with a
echo  real product brief. Every step shown:
echo    1. The input brief
echo    2. The agent running on free OpenRouter models
echo    3. The full 6-email output
echo.
echo  Ready? Press any key to begin...
pause >nul

echo.
echo  =============================================================
echo   STEP 1: THE INPUT BRIEF
echo  =============================================================
echo.
echo  Product:   $197 6-week productivity course for solo SaaS founders
echo  Tagline:   Ship the boring features without burning out
echo  Audience:  4,200 indie devs, mostly solo SaaS founders
echo  Launch:    Cart opens Monday, closes Friday
echo  Bonus:     1:1 review session for first 20 buyers
echo  Voice:     Direct, technical, no fluff
echo.
echo  Press any key to submit this to the agent...
pause >nul

echo.
echo  =============================================================
echo   STEP 2: RUNNING THE AGENT
echo  =============================================================
echo.
echo  Model: meta-llama/llama-3.3-70b-instruct (free tier)
echo  Fallback: 7 models — if one rate-limits, next takes over
echo  Cost: $0 — OpenRouter free tier
echo.
echo  Calling the agent now...
echo.

:: Run from the pack root directory
cd /d "%~dp0"

:: Pipe the brief into the agent via stdin, ending with END sentinel
(
echo $197 6-week productivity course for solo SaaS founders. Tagline: ship the boring features without burning out. List of 4,200 mostly indie devs. Cart opens Monday, closes Friday at midnight. Bonus: 1:1 review session for first 20 buyers. Voice: direct, technical, no fluff.
echo END
) | python "%~dp0launch_email_sequencer\agent.py"

echo.
echo  =============================================================
echo   THAT'S THE LAUNCH EMAIL SEQUENCER
echo  =============================================================
echo.
echo  Output includes:
echo    - 6-email launch sequence with subjects 7 timing
echo    - Copy written in your exact voice
echo    - Urgency CTA tied to your bonus
echo    - Abandonment follow-up for cart abandoners
echo    - Post-close recap
echo.
echo  All for $0/month to run.
echo.
echo  The other 6 agents work the same way:
echo.
echo    run_sales_page_critique.bat     Paste a sales page, get specific fixes
echo    run_refund_deescalator.bat      Paste a refund request, get a tactful reply
echo    run_customer_qa.bat             Paste a buyer Q, get an honest answer
echo    run_affiliate_outreach.bat      Paste terms + prospect, get a personalized pitch
echo    run_testimonial_collector.bat  Paste a buyer, get the right ask + follow-ups
echo    run_lesson_outliner.bat         Paste a topic, get a full outline with hooks
echo.
echo  =============================================================
echo   GET THE PACK: [YOUR_GUMROAD_LINK]
echo   Launch price: $39  —  $49 after launch
echo   No monthly fee. No SaaS. Own it forever.
echo  =============================================================
echo.
echo  Press any key to exit...
pause >nul
