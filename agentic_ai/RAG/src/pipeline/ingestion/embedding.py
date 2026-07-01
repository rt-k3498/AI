#from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
import os


openAI_api_key = os.getenv("OPENAI_API_KEY")

class EmbeddingGenerator:
    def __init__(self, model_name: str = "text-embedding-3-small", dimensions: int = 1024):
        self.embeddings = OpenAIEmbeddings(
            model=model_name,
            api_key=openAI_api_key,
            dimensions=dimensions
        )

    def generate_embeddings(self, text: str) -> list[float]:
        return self.embeddings.embed_query(text)