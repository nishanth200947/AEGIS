# PROJECT AEGIS
# Mission 004 - Main Controller

from config import AEGIS_NAME, VERSION, MODE
from logger import start_log


def system_start():

    start_log()

    print("==============================")
    print(AEGIS_NAME)
    print("Version:", VERSION)
    print("Mode:", MODE)
    print("Core System Initialized")
    print("==============================")


if __name__ == "__main__":
    system_start()