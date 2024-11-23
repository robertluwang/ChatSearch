# llm_factory.py
class LLMFactory:
    _registry = {}

    @staticmethod
    def register_llm(name, llm_class):
        """
        Register a new LLM class with a unique name.
        """
        LLMFactory._registry[name] = llm_class
        print(f"[DEBUG] LLM registered: {name}")

    @staticmethod
    def create_llm(name, **kwargs):
        """
        Create an instance of a registered LLM by name.
        """
        print(f"[DEBUG] Registered models: {list(LLMFactory._registry.keys())}")
        print(f"[DEBUG] Attempting to create model: {name} with arguments: {kwargs}")

        if name not in LLMFactory._registry:
            raise ValueError(f"Model '{name}' is not registered. Available models: {list(LLMFactory._registry.keys())}")

        return LLMFactory._registry[name](**kwargs)
