# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:48:33 2026

@author: fisch
"""

import subprocess
import time
import sys

# Pfade anpassen falls nötig
FASTAPI_CMD = [
    sys.executable, "-m", "uvicorn",
    "Backend.main:app",
    "--reload",
    "--port", "8000"
]

STREAMLIT_CMD = [
    sys.executable, "-m", "streamlit",
    "run",
    "Frontend/app.py"
]

def start_backend():
    return subprocess.Popen(FASTAPI_CMD)

def start_frontend():
    return subprocess.Popen(STREAMLIT_CMD)

if __name__ == "__main__":
    print("Starting Rocky App...")

    backend = start_backend()

    # kleiner delay damit API hochfährt
    time.sleep(5)

    frontend = start_frontend()

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("Shutting down...")
        backend.terminate()
        frontend.terminate()