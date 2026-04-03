from fastapi import APIRouter
from app.services.rag_pipeline import generate_answer

router = APIRouter()

@router.get("/query")
def query(q: str):
    answer = generate_answer(q)
    return answer