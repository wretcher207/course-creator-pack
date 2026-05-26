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
echo  Product:   $39 Course Creator Pack for info-product creators
echo  Tagline:   Ship the writing, support, and launch busywork — not the course
echo  Audience:  11,200 course creators, coaches, and info-product sellers
echo  Launch:    Cart opens Tuesday, closes Friday at midnight
echo  Bonus:     7 bonus scripts for early buyers
echo  Voice:     Direct, no fluff, treats buyers like smart people
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
echo $39 Course Creator Pack for info-product creators. Tagline: ship the writing, support, and launch busywork — not the course. List of 11,200 course creators, coaches, and info-product sellers. Cart opens Tuesday, closes Friday at midnight. Bonus: 7 bonus scripts for early buyers. Voice: direct, no fluff, treats buyers like smart people.
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
echo   GET THE PACK: https://GiganticDadPants.gumroad.com/l/jrlmrg
echo   Price: $39  —  $49 after launch
echo   No monthly fee. No SaaS. Own it forever.
echo  =============================================================
echo.
echo  Press any key to exit...
pause >nul
