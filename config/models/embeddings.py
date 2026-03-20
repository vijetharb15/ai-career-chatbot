import os

from langchain_core.embeddings.fake import DeterministicFakeEmbedding

def get_embeddings():
    return DeterministicFakeEmbedding(size=1536)

