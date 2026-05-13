from services.dataEmbeddingPipeline import dataEmbeddingPipeline
from pathlib import Path

folder = Path(r".\data")

directories = [p for p in folder.iterdir() if p.is_file()]


dataEmbeddingPipeline(directories)