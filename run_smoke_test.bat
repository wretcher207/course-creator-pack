@echo off
REM End-to-end smoke test: hits OpenRouter once per agent (~7 free-tier calls).
cd /d "%~dp0"
if not exist venv\Scripts\python.exe (
  echo venv missing. Run setup.bat first.
  pause
  exit /b 1
)
call venv\Scripts\activate.bat
python smoke_test.py
echo.
pause
