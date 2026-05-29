import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="GenAI Chatbot", layout="wide")

st.title("🤖 GenAI Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "You are a helpful AI assistant."

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    system_prompt = st.text_area(
        "System Prompt",
        value=st.session_state.system_prompt
    )
    
    if st.button("Update Prompt"):
        st.session_state.system_prompt = system_prompt
    
    if st.button("Clear Chat"):
        st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Add system prompt at beginning
    messages = [
        {"role": "system", "content": st.session_state.system_prompt}
    ] + st.session_state.messages

    response = get_response(messages)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)