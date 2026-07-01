from .loaders import PDFLoader, HTMLLoader, TextLoader
from .chunkers import RecursiveCharacterChunker
from .embedding import EmbeddingGenerator
from ..._storage_client.supabase import supabase

pdf_loader = PDFLoader()
chunker = RecursiveCharacterChunker(file_type="pdf")
embedding_generator = EmbeddingGenerator()

document = pdf_loader.load("/Users/artyk./Other_folders/SoftwareDev/AI/agentic_ai/RAG/data/pdf/Bachelor_s_Thesis___Arty.pdf")
print(f"Number of documents: {len([document])}")

document_chunks = chunker.chunk(document)
print(f"Number of document chunks: {len(document_chunks)}")

rows = []

for i, chunk in enumerate(document_chunks):
    embeddings = embedding_generator.generate_embeddings(chunk.page_content)
    rows.append(
        {
            "content": chunk.page_content,
            "metadata": chunk.metadata,
            "vectors": embeddings,
        }
    )

print(f"Done generating embeddings for document chunks.")

res = supabase.table("documents").insert(rows).execute()

print("Done inserting document chunks into DB.")


