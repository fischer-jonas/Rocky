# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:21:42 2026

@author: fisch
"""

import streamlit as st
import requests
import time

st.set_page_config(page_title="Rocky Chat", page_icon="👽")

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