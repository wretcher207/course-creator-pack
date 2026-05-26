@echo off
chcp 65001 >nul 2>&1
cd /d "%~dp0"
if not exist venv\Scripts\python.exe (
  echo venv missing. Run setup.bat first.
  pause
  exit /b 1
)
call venv\Scripts\activate.bat
python -m refund_deescalator.agent --stdin < "%~dp0run_refund_deescalator_input.txt"
echo.
pause