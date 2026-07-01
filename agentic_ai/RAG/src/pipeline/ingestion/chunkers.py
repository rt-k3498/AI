from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from abc import ABC, abstractmethod
from typing import Literal

type DocumentType = Literal["text", "pdf", "html"]

class Chunker(ABC):
    @abstractmethod
    def chunk(self, document: str) -> list[str]:
        pass


class RecursiveCharacterChunker(Chunker):
    def __init__(self, file_type: DocumentType, chunk_size: int = 1000, chunk_overlap: int = 200):
        recursive_rule = None
        match file_type:
            case "text":
                recursive_rule = ["\n\n", "\n", " ", ""]
            case "pdf":
                recursive_rule = ["\n\n", "\n", " ", ""]
            case "html":
                recursive_rule = ["</article>", "</section>", "</main>", "</div>", "</table>", "</ul>", "</ol>", "</li>", "</p>", "<br>", "\n\n", "\n", ". ", " ", ""]
            case _:
                raise ValueError(f"Unsupported file type: {file_type}")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap, separators=recursive_rule
        )

    def chunk(self, document: Document) -> list[Document]:
        return self.text_splitter.split_documents([document])

