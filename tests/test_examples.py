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
    assert exit_code == 0
    assert out == "test1\ntest2\n"
    assert err == ""
