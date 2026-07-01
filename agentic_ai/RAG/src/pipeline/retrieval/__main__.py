from .RAGRetriever import RAGRetriever
from ..ingestion.embedding import EmbeddingGenerator


def retrieve_context(query: str, top_k: int = 5, similarity_threshold: float = 0.1):
    embedding_generator = EmbeddingGenerator()
    retriever = RAGRetriever(embedding_generator=embedding_generator)
    return retriever.retrieve(query, top_k=top_k, similarity_threshold=similarity_threshold)


if __name__ == "__main__":
    query = "what is federated learning?"
    context_documents = retrieve_context(query)
    print(context_documents)
