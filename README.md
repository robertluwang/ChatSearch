# ChatSearch: Real-Time Web Search & Multi-LLM Support Chatbot

This repository presents a chatbot capable of engaging in real-time conversations enriched with information retrieved directly from the internet. Its key strength lies in its support for multiple Large Language Models (LLMs), offering flexibility and ease of extension.

## Key Features
- Real-Time Web Search: Unlike chatbots limited to pre-existing knowledge bases, this chatbot dynamically searches the internet using DuckDuckGo's API to access up-to-the-minute information, ensuring its responses are current and relevant.

- Multi-LLM Support: The architecture is designed to seamlessly integrate with various LLMs, including (but not limited to) Google Gemini, Ollama, and OpenAI models. Adding support for new LLMs requires minimal code changes, promoting adaptability and allowing you to leverage the strengths of different models.

- Source Attribution: Provides transparent source attribution for all information used in generating responses, fostering trust and allowing users to verify the chatbot's claims.

- Modular Design: The codebase is built with modularity in mind, making it simple to maintain, expand, and customize.

## Installation
```
python3 -m venv .venv  # Creates a virtual environment
source .venv/bin/activate  # Activates the virtual environment (Linux/macOS)
.venv\Scripts\activate     # Activates the virtual environment (Windows)
pip install -r requirements.txt
```

## Demo app
```
streamlit run streamlit_app.py
```