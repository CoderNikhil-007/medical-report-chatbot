from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

# ✅ Lazy import for upload
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    from services.pdf_processor import process_pdf  # lazy import

    content = await file.read()
    result = process_pdf(content)

    return {"message": "File processed successfully"}

# ✅ Lazy import for query
@app.get("/query")
def query(q: str):
    from services.rag_pipeline import generate_answer  # lazy import

    return generate_answer(q)