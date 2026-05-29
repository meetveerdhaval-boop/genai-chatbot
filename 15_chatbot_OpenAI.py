# pip install openai streamlit python-dotenv
# to run: streamlit run 4_chatbot_OpenAI.py
from openai import OpenAI
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.title("ChatGPT-like clone")

client = OpenAI(api_key=OPENAI_API_KEY)

# check if model is set in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# check if messages are set in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# accept user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        # display the stream of response chunks
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
