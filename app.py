
from google import genai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

st.title("Chatbot")

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Chat input
prompt = st.chat_input("Ask anything")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    try:
        interaction = client.interactions.create(
            model="gemini-2.5-flash",
            input=prompt
        )

        with st.chat_message("assistant"):
            st.write(interaction.output_text)

    except Exception as e:
        st.error(f"Error: {e}")
