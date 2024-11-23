# chatsearch.py
import time
import re
from llm_factory import LLMFactory
from duckduckgo_api_haystack import DuckduckgoApiWebSearch

class ChatSearch:
    def __init__(self, model_type='gemini', model_name='models/gemini-1.5-pro-002', top_k=10, **kwargs):
        self.debug = True
        print(f"[DEBUG] Initializing ChatSearch with model_type={model_type}, model_name={model_name}")
        self.model_type = model_type
        self.model_name = model_name
        self.top_k = top_k
        self.websearch = DuckduckgoApiWebSearch(top_k=self.top_k)
        self.llm = LLMFactory.create_llm(model_type, model_name=model_name, **kwargs)

    @staticmethod
    def _enforce_source_markers(response_text, source_links):
        """
        Ensures the response includes source markers. Appends all sources if none are present.
        """
        source_marker_pattern = r"\[\d+\]"
        if not re.search(source_marker_pattern, response_text):
            response_text += "\n\nSources: " + ", ".join(source_links)
        return response_text

    def update_model(self, model_type, model_name, **kwargs):
        print(f"[DEBUG] Updating ChatSearch to model_type={model_type}, model_name={model_name}")
        self.model_type = model_type
        self.model_name = model_name
        self.llm = LLMFactory.create_llm(model_type, model_name=model_name, **kwargs)

    def search_and_generate(self, query):
        """
        Performs a web search and generates a response using the selected LLM.
        """
        time.sleep(1)  # Add delay before the web search API call

        # Re-initialize websearch with the current top_k value
        self.websearch = DuckduckgoApiWebSearch(top_k=self.top_k)

        # Perform web search
        results = self.websearch.run(query=query)

        # Access search results
        documents = results["documents"]
        links = results["links"]

        # Prepare documents with source markers
        document_contents = [
            f"[{i + 1}] {doc.content}" for i, doc in enumerate(documents)
        ]
        combined_documents = "\n\n".join(document_contents)

        # Prepare source links with markers
        source_links = [
            f"[{i + 1}] {doc.meta['link']}" for i, doc in enumerate(documents)
        ]

        # Build context for the LLM
        context = (
            f"Query: {query}\n\n"
            "Please provide an answer based on the information below. Use the source markers (e.g., [1], [2]) "
            "to indicate the source of your information. Each claim should be attributed to its corresponding source.\n\n"
            f"Relevant Information:\n{combined_documents}"
        )

        # Generate response
        generated_text = self.llm.generate_content(context)

        # Enforce source markers
        final_response = self._enforce_source_markers(generated_text, source_links)

        # Format source links as a Markdown list
        formatted_sources = "\n".join([f"- {link}" for link in source_links])

        # Combine the response with the formatted sources
        final_output = f"{final_response}\n\n### Grounding Sources:\n{formatted_sources}"

        return final_output
    
    