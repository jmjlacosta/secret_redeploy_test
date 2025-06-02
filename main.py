import os
import openai
import streamlit as st

st.set_page_config(page_title="Chat with GPT", layout="centered")

st.sidebar.title("Chat with GPT")
st.sidebar.markdown("Secure, conversational interface to GPT")

st.title("🧠 Chat with GPT")

openai.api_key = os.environ.get("OPENAI_API_KEY")

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.chat_input("Ask something...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = ask_gpt(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
