import faiss
import numpy as np

index = None
stored_chunks = []

def create_index(embeddings, chunks):
    global index, stored_chunks

    dim = len(embeddings[0])
    
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    stored_chunks = chunks


def search(query_embedding, top_k=3):
    D, I = index.search(query_embedding, top_k)
    
    return [stored_chunks[i] for i in I[0]]