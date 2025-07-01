
import streamlit as st
import os
from app import ai_response

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User input
user_msg = st.chat_input("Ask something")

if user_msg:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_msg})
    with st.chat_message("user"):
        st.write(user_msg)

    # AI response
    ai_reply = ai_response(user_msg)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)
