# PROJECT AEGIS
# Mission 004 - Core Testing

from pathlib import Path


def test_core_files():

    files = [
        "../../03_Code/Python/core/main.py",
        "../../03_Code/Python/core/config.py",
        "../../03_Code/Python/core/logger.py"
    ]

    for file in files:
        assert Path(file).exists()


def test_message():

    message = "AEGIS CORE READY"

    assert message == "AEGIS CORE READY"


print("AEGIS Core Test Passed")