from db.entityModels.document import Document
from db.database import get_connection
import logging

logger = logging.getLogger(__name__)

def insert_document(document: Document):
    with get_connection() as conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO documents (path) VALUES (%s)", (document.path,))
                conn.commit()
                row = cursor.fetchone()
                
                return row[0] if row else None
        except Exception:
            conn.rollback()
            logger.exception("Failed to insert document into DB")
            raise




async def insert_document_async(document: Document):
    async with get_connection() as conn:
        try:
            async with conn.cursor() as cursor:
                await cursor.execute(
                    "INSERT INTO documents (path) VALUES (%s) RETURNING id",
                    (document.path,)
                )

                row = await cursor.fetchone()
                await conn.commit()

                return row[0] if row else None

        except Exception:
            await conn.rollback()
            logger.exception("Failed to insert document into DB")
            raise