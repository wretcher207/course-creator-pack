"""Find the OpenRouter API key from one of three places, in order."""
import os
import re
from pathlib import Path

DESKTOP_KEY_FILE = Path.home() / "Desktop" / "openrouter-api.txt"
PROJECT_ENV = Path(__file__).resolve().parent.parent / ".env"


def _read_env_file(path: Path) -> str | None:
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("OPENROUTER_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def _read_desktop_file(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r"sk-or-v1-[A-Za-z0-9]+", text)
    return match.group(0) if match else None


def load_api_key() -> str:
    """Resolution order:
    1. Desktop file at ~/Desktop/openrouter-api.txt (any line containing the key)
    2. Project .env file
    3. OPENROUTER_API_KEY environment variable
    """
    key = _read_desktop_file(DESKTOP_KEY_FILE)
    if key:
        return key

    key = _read_env_file(PROJECT_ENV)
    if key and not key.startswith("sk-or-v1-..."):
        return key

    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key

    raise RuntimeError(
        f"OpenRouter API key not found. Put it in {DESKTOP_KEY_FILE}, "
        f"create {PROJECT_ENV}, or set OPENROUTER_API_KEY env var."
    )
