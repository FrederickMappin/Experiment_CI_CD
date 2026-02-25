
import subprocess
import sys


def test_cli_add():
    result = subprocess.run([
        sys.executable, "main.py", "add", "2", "2"
    ], capture_output=True, text=True)
    assert "2.0 + 2.0 = 4.0" in result.stdout
    assert "Negated result: -4.0" in result.stdout


def test_cli_negate():
    result = subprocess.run([
        sys.executable, "main.py", "negate", "5"
    ], capture_output=True, text=True)
    assert "-5.0" in result.stdout
