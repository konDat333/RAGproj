from pydantic import BaseModel
from typing import Any
from pydantic import Field


class TextChunk(BaseModel):
    text: str
    metadata: dict[str, Any] = Field(default_factory=dict)
