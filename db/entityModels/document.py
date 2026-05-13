from pydantic import BaseModel

class Document(BaseModel):
    id: int | None = None
    path: str
