# openai_llm.py
from llm_factory import LLMFactory
import openai

class OpenAILLM:
    def __init__(self, api_key: str, model_name: str):
        openai.api_key = api_key
        self.model_name = model_name
        print(f"[DEBUG] Initializing OpenAILLM with model: {model_name}")

    def generate_content(self, context: str) -> str:
        print(f"[DEBUG] Generating content using OpenAILLM for context: {context[:50]}...")
        response = openai.Completion.create(
            model=self.model_name,
            prompt=context,
            max_tokens=500
        )
        return response.choices[0].text.strip()

LLMFactory.register_llm('openai', OpenAILLM)