# gemini_llm.py

from llm_factory import LLMFactory
import google.generativeai as genai

class GeminiLLM:
    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key
        print(f"[DEBUG] Initializing GeminiLLM with model: {model_name}")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_content(self, context: str) -> str:
        print(f"[DEBUG] Generating content using GeminiLLM for context: {context[:50]}...")
        response = self.model.generate_content(context)
        return response.text

LLMFactory.register_llm('gemini', GeminiLLM)