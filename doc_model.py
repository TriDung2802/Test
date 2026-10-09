from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Document:
    content: str
    doc_id: str= "" 
    title: str= ""
    source: str= ""
    metadata: dict = field(default_factory = dict)
    created_at: Optional[datetime] = field(default_factory=datetime.now)

@dataclass
class DocumentChunk:
    content: str
    chunk_id: str = ""
    doc_id: str = ""
    chunk_index: int = 0
    metadata: dict = field(default_factory = dict)
    embedding: Optional[list[float]] = None

def chunk_document(doc:Document, chunk_size: int =512, overlap: int = 64 ) -> list[DocumentChunk]:
    chunks=[]
    text=doc.content
    start=0
    index=0
    while start < len(text):

        end = start + chunk_size
        chunk_text = text[start:end]

        chunk = DocumentChunk(
            content=chunk_text,
            chunk_id=f"{doc.doc_id}_{index}",
            doc_id=doc.doc_id,
            chunk_index=index,
            metadata=doc.metadata.copy()
        )

        chunks.append(chunk)

        start = end - overlap
        index += 1

    return chunks
