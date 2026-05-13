from pathlib import Path

from db.entityModels.document import Document
from db.entityModels.document_chunk import DocumentChunk
from db.repos.document_chunk_CRUD import insert_document_chunk
from db.repos.document_CRUD import insert_document
from services.chunking import chunk_file
from services.embedding import embed_text


def dataEmbeddingPipeline(paths: list[Path]):
    for path in paths:
        document = Document(id=None, path=str(path))
        document_id = insert_document(document)
        if document_id is not None:
            chunks = chunk_file(
                path,
                extra_metadata={"source_path": str(path), "document_id": document_id},
            )
            for chunk in chunks:
                embedding = embed_text(chunk.text)
                insert_document_chunk(
                    DocumentChunk(
                        content=chunk.text,
                        embedding=embedding,
                        metadata=chunk.metadata,
                        document_id=document_id,
                    )
                )
        else:
            raise Exception("Failed to insert document into DB")
