from pydantic import BaseModel, Field

class DocumentChunk(BaseModel):
    id: int
    content: str
    embedding: list[float] = Field(default_factory=list)
    metadata: dict = Field(default_factory=dict)
    document_id: int