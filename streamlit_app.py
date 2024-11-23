# streamlit_app.py

import os
import streamlit as st
from dotenv import load_dotenv
from chatsearch import ChatSearch

# Explicitly import LLM modules to ensure registration
import gemini_llm
import ollama_llm
import openai_llm

# Load environment variables
load_dotenv()

# Available LLMs and models
AVAILABLE_MODELS = {
    'gemini': ['models/gemini-1.5-pro-002', 'models/gemini-1.5-flash'],
    'ollama': ['ollama-model-1', 'ollama-model-2'],
    'openai': ['text-davinci-003', 'gpt-3.5-turbo']
}

# Streamlit App
st.title("ChatSearch with Multi-LLM Support")

# Sidebar settings
llm_type = st.sidebar.selectbox('Select LLM Type', list(AVAILABLE_MODELS.keys()))
model_name = st.sidebar.selectbox('Select Model', AVAILABLE_MODELS[llm_type])
top_k = st.sidebar.slider("Number of search results", 2, 20, 10)

api_key = os.getenv("GOOGLE_API_KEY") if llm_type in ['gemini', 'openai'] else None

try:
    st.sidebar.write("Initializing ChatSearch...")
    chat_search = ChatSearch(model_type=llm_type, model_name=model_name, top_k=top_k, api_key=api_key)
    st.sidebar.success("ChatSearch initialized successfully.")
except Exception as e:
    st.sidebar.error(f"Initialization failed: {e}")
    st.stop()

query = st.text_input("Enter your query:")
if st.button("Search and Generate Answer"):
    if query.strip():
        try:
            result = chat_search.search_and_generate(query)
            st.markdown(result)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query.")


