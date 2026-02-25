
import subprocess
import sys


def test_smoke_add():
    result = subprocess.run([
        sys.executable, "main.py", "add", "1", "1"
    ], capture_output=True, text=True)
    assert "add" in result.stdout


def test_smoke_subtract():
    result = subprocess.run([
        sys.executable, "main.py", "subtract", "2", "1"
    ], capture_output=True, text=True)
    assert "subtract" in result.stdout or "-" in result.stdout


def test_smoke_negate():
    result = subprocess.run([
        sys.executable, "main.py", "negate", "1"
    ], capture_output=True, text=True)
    assert "Negate" in result.stdout
