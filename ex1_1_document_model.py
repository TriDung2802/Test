from dataclasses import dataclass, field
from datetime import datetime
from doc_model import Document,DocumentChunk
from typing import Optional
doc=Document(
    content="""Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It emphasizes code readability with its notable use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library. It has become one of the most popular programming languages, particularly in data science, artificial intelligence, and web development.""",
    doc_id="DOC001",
    title="Introduction to Python",
    source="course_materials"
)

print(f"Document: {doc.title} ({doc.doc_id})")
print (f"Content length: {len(doc.content)} chars\n")

def chunk_document(doc:Document,chunk_size:int=150,overlap:int=30)->list[DocumentChunk]:
    chunks=[]
    text=doc.content
    start=0
    while start<len(text):
        end=min(start+chunk_size,len(text))
        chunk_text=text[start:end]
        chunk=DocumentChunk(
            content=chunk_text,
            chunk_id=f"{doc.doc_id}_chunk_{len(chunks)}",
            doc_id=doc.doc_id,
            chunk_index=len(chunks),
            metadata={**doc.metadata,"chunk_size":chunk_size,"overlap":overlap}
        )
        chunks.append(chunk)
        start+=chunk_size-overlap
        if start >=len(text):
            break
    return chunks
chunks=chunk_document(doc,chunk_size=150,overlap=30)
print(f"Created {len(chunks)} chunks:\n")
for chunk in chunks:
    print(f"[{chunk.chunk_id}] (index{chunk.chunk_index})")
    print(f"Text: {chunk.content}...")
    print(f"Length: {len(chunk.content)} chars")
    print()