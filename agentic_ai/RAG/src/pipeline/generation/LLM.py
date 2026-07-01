from langchain_openai import OpenAI

class LLM:
    def __init__(self, model_name: str = "gpt-4o-mini-2024-07-18", temperature: float = 0.1, max_tokens: int = 1024):
        self.llm = OpenAI(
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )

    def prompt(self, prompt: str) -> str:
        return self.llm.generate([prompt]).generations[0][0].text