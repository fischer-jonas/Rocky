# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:21:42 2026

@author: fisch
"""

import streamlit as st
import random, os
import requests
import time

st.set_page_config(page_title="Rocky Chat", page_icon="👽")


media_folder = os.path.join(os.path.dirname(__file__), "..", "Media")
gif_files = [f for f in os.listdir(media_folder) if f.endswith(".gif")]
random_gif = random.choice(gif_files)
if "rocky_gif" not in st.session_state:
    st.session_state.rocky_gif = random.choice(gif_files)
gif_path = os.path.join(media_folder, random_gif)
with open(gif_path, "rb") as f:
    gif_bytes = f.read()


st.image(gif_bytes)


st.title("Talk to Rocky (English - Eridian Translator) ♪")

#Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

#Chat Verlauf 
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Say something to Rocky...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Backend Call
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_input}
    )

    reply = response.json()["reply"]

    # Assistant Message speichern
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
    
        for word in reply.split():
            full_response += word + " "
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
    
        message_placeholder.markdown(full_response)