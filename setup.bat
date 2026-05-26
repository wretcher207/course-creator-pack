@echo off
REM First-time setup: create venv and install dependencies.
REM Double-click this file once. After that, use the run_*.bat files.

cd /d "%~dp0"

echo === Creating virtual environment ===
py -m venv venv
if errorlevel 1 (
  echo Failed to create venv. Is Python installed? Try: https://www.python.org/downloads/
  pause
  exit /b 1
)

echo === Installing dependencies ===
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 (
  echo Failed to install requirements.
  pause
  exit /b 1
)

echo.
echo === Setup complete ===
echo You can now double-click any of the run_*.bat files.
echo.
pause
