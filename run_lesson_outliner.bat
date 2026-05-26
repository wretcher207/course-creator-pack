@echo off
chcp 65001 >nul 2>&1
cd /d "%~dp0"
if not exist venv\Scripts\python.exe (
  echo venv missing. Run setup.bat first.
  pause
  exit /b 1
)
call venv\Scripts\activate.bat
python -m lesson_outliner.agent --stdin < "%~dp0run_lesson_outliner_input.txt"
echo.
pause