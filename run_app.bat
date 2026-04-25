@echo off
echo Starting Rocky App...

REM activate conda environment
call C:\Users\fisch\anaconda3\Scripts\activate.bat rocky

REM start backend (FastAPI)
start cmd /k python -m uvicorn Backend.main:app --reload --port 8000

REM wait a bit
timeout /t 5 > nul

REM start frontend (Streamlit)
start cmd /k python -m streamlit run Frontend/app.py

echo Rocky is running! ♪
pause