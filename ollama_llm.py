# ollama_llm.py
from llm_factory import LLMFactory
import subprocess

class OllamaLLM:
    def __init__(self, model_name: str):
        self.model_name = model_name
        print(f"[DEBUG] Initializing OllamaLLM with model: {model_name}")

    def generate_content(self, context: str) -> str:
        print(f"[DEBUG] Generating content using OllamaLLM for context: {context[:50]}...")
        result = subprocess.run(
            ['ollama', 'chat', '--model', self.model_name, '--input', context],
            capture_output=True, text=True
        )
        return result.stdout.strip()

LLMFactory.register_llm('ollama', OllamaLLM)