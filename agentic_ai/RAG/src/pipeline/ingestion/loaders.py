from langchain_core.documents import Document
import pypdf


class PDFLoader:
    def __init__(self):
        pass

    def load(self, file_path: str) -> Document:
        pdf_reader = pypdf.PdfReader(file_path)
        pages = []

        for page_number, page in enumerate(pdf_reader.pages, start=1):
            text = page.extract_text() or ""
            if text:
                pages.append(f"[Page {page_number}]\n{text}")

        return Document(
            page_content="\n\n".join(pages),
            metadata={
                "source": file_path,
                "filename": file_path.split("/")[-1],
                "page_count": len(pdf_reader.pages),
            },
        )

class HTMLLoader:
    def __init__(self):
        pass

    def load(self, file_path: str) -> Document:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return Document(
            page_content=content,
            metadata={
                "source": file_path,
                "filename": file_path.split("/")[-1],
            },
        )
    
class TextLoader:
    def __init__(self):
        pass

    def load(self, file_path: str) -> Document:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return Document(
            page_content=content,
            metadata={
                "source": file_path,
                "filename": file_path.split("/")[-1],
            },
        )