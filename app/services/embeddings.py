from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_documents(docs, chunk_size=500, overlap=100):
    chunks = []

    for doc in docs:
        text = doc["text"]
        page = doc["page"]

        for i in range(0, len(text), chunk_size - overlap):
            chunks.append({
                "text": text[i:i + chunk_size],
                "page": page
            })

    return chunks


def get_embeddings(chunks):
    texts = [chunk["text"] for chunk in chunks]
    return model.encode(texts)