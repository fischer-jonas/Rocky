\# Rocky Chatbot



An interactive AI chatbot that simulates \*\*Rocky\*\* from \*Project Hail Mary\* using a local LLM via Ollama, FastAPI, and Streamlit.



The chatbot features:

\- Rocky-style personality (broken, friendly, repetitive speech)

\- Animated GIF character display

\- Random sound effects per response

\- Local AI inference (no API costs) and runable far away at Tau-Ceti

\- One-click startup for Windows





Start the app and chat with Rocky:

> “Hello hello! ♪ Friend human!”



\---



\## Architecture

Streamlit UI -->FastAPI Backend -->Ollama LLM (Llama 3)



\## Installation



\### 1. Clone repository

```bash

git clone https://github.com/fischer-jonas/Rocky

cd Rocky

conda create -n rocky python=3.10 -y

conda activate rocky

pip install fastapi uvicorn streamlit requests

Download \& Install ollama from https://ollama.com/

ollama pull llama3



\## Start application

Option 1: 

Windows Double-Click: run\_app.bat (Change Path accordingly)



Option 2:

Python script: conda activate rocky

python run\_app.py



Option 3:

Manual starts: 

uvicorn Backend.main:app --reload --port 8000

streamlit run Frontend/app.py



\## Author

Jonas Fischer



