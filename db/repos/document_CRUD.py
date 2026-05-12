from db.models.document import Document
from db.database import get_connection

def insert_document(document: Document):
    with get_connection() as conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO documents (path) VALUES (%s)", (document.path,))
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise e