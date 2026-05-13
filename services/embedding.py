from sentence_transformers import SentenceTransformer
import asyncio

model = SentenceTransformer(
    "sentence-transformers/msmarco-distilbert-dot-v5"
)

def embed_text(text: str) -> list[float]:
    try:
        return model.encode(text, normalize_embeddings=True).tolist()
    except Exception as e:
        return list[float]([0.0] * 1536)



async def embed_text(text: str) -> list[float]:
    try:
        vec = await asyncio.to_thread(
        model.encode,
        text,
        normalize_embeddings=True)
        return vec.tolist()
    except Exception as e:
        return list[float]([0.0] * 1536)