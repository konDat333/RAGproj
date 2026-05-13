from db.entityModels.document_chunk import DocumentChunk
from db.database import get_connection
import asyncio

async def insert_document_chunk_async(document_chunk: DocumentChunk):
    async with get_connection() as conn:
        try:
            async with conn.cursor() as cursor:
                await cursor.execute("INSERT into document_chunks (content,embedding,metadata,document_id) VALUES (%s,%s,%s,%s)", 
                (document_chunk.content,document_chunk.embedding,document_chunk.metadata,document_chunk.document_id))
                await conn.commit()
        except Exception as e:
            await conn.rollback()
            raise e


def insert_document_chunk(document_chunk: DocumentChunk):
    with get_connection() as conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("INSERT into document_chunks (content,embedding,metadata,document_id) VALUES (%s,%s,%s,%s)", 
                (document_chunk.content,document_chunk.embedding,document_chunk.metadata,document_chunk.document_id))
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise e