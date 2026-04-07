from fastapi import APIRouter


router = APIRouter()

@router.get("/query")
def query(q: str):
    from app.services.rag_pipeline import generate_answer
    answer = generate_answer(q)
    return answer