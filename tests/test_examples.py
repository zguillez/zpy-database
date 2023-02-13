import subprocess
import os
import sys


def capture(command):
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
    out, err = proc.communicate()
    exit_code = proc.returncode
    return exit_code, out.decode('utf-8'), err.decode('utf-8')


def test_test():
    os.environ["PYTHONPATH"] = "."
    exit_code, out, err = capture([sys.executable, "examples/main.py"])
    if 'DB_HOST' in os.environ and 'DB_NAME' in os.environ and 'DB_USER' in os.environ and 'DB_PASS' in os.environ:
        assert exit_code == 0
        assert out == "Marcilla\n"
        assert err == ""
    else:
        assert exit_code == 1
        assert out == ""
        assert err != ""
