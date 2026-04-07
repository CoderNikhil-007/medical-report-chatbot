from fastapi import APIRouter, UploadFile
import os

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile):
    from app.services.pdf_loader import extract_text_with_metadata
    from app.services.embeddings import chunk_documents, get_embeddings
    from app.services.vector_store import create_index
    file_path = f"data/{file.filename}"
    
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # ✅ NEW FLOW
    docs = extract_text_with_metadata(file_path)
    chunks = chunk_documents(docs)
    embeddings = get_embeddings(chunks)

    create_index(embeddings, chunks)

    return {"message": "File processed successfully"}