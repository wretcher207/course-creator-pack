@echo off
chcp 65001 >nul 2>&1
cd /d "%~dp0"
if not exist venv\Scripts\python.exe (
  echo venv missing. Run setup.bat first.
  pause
  exit /b 1
)
call venv\Scripts\activate.bat
python -m customer_qa.agent --stdin < "%~dp0run_customer_qa_input.txt"
echo.
pause