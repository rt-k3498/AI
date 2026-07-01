from ..._storage_client.supabase import supabase
from ..._storage_client.pg import PGPooler
from ..ingestion.embedding import EmbeddingGenerator

class RAGRetriever:
    def __init__(self, supabase_client = supabase, embedding_generator = EmbeddingGenerator()):
        self.supabase = supabase_client
        self.embedding_generator = embedding_generator

    def retrieve(self, query, top_k=5, similarity_threshold=0.1):
        # Generate embeddings for the query
        query_embedding = self.embedding_generator.generate_embeddings(query)

        # Retrieve documents from Supabase based on the query embedding
        response = self.supabase.rpc("match_vectors", {
            "query_vector": query_embedding,
            "top_k": top_k, 
            "similarity_threshold": similarity_threshold
        }).execute()

        return response.data
