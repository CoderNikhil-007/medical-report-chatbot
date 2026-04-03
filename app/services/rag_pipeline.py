import google.generativeai as genai
from .embeddings import model
from .vector_store import search
from .memory import add_to_memory, get_memory
from dotenv import load_dotenv
import os

load_dotenv() 

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model_llm = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(query: str):
    
    last_memory = get_memory(limit=1)

    if last_memory:
        last_q = last_memory[-1]["question"]
        enhanced_query = f"{query} (context: {last_q})"
    else:
        enhanced_query = query

    query_embedding = model.encode([enhanced_query])

    relevant_chunks = search(query_embedding, top_k=2)

    context = ""
    sources = []

    for chunk in relevant_chunks:
        context += chunk["text"] + "\n"
        sources.append(f"Page {chunk['page']}")

    sources_text = ", ".join(set(sources))

    memory = get_memory(limit=4)

    memory_text = ""
    for m in memory:
        memory_text += f"Q: {m['question']}\nA: {m['answer']}\n"

    memory_text = memory_text[:800]

    prompt = f"""
        You are a medical report assistant.

        STRICT RULES:
        - Answer ONLY from the given context with a SHORT explanation
        - Use previous conversation if relevant
        - If answer not present, say: Not available in report
        - Keep answer short (1-2 lines)
        - Do NOT give medical advice
        - Do NOT mention sources
        - Do NOT generate follow-up questions

        Previous Conversation:
        {memory_text}

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

    try:
        response = model_llm.generate_content(prompt)
        answer = response.text.strip()
    except Exception as e:
        return {
            "answer": f"Error: {str(e)}",
            "sources": ""
        }

    answer = answer.split("\n")[0].strip()

    add_to_memory(query, answer)

    return {
        "answer": answer,
        "sources": sources_text
    }