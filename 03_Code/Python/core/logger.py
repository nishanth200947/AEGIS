# PROJECT AEGIS
# Mission 004 - Logging System

from datetime import datetime


def start_log():
    current_time = datetime.now()

    print("[AEGIS LOG]")
    print("Time:", current_time)
    print("System Logger Initialized")