# 🩺 Medical Report Chatbot (RAG + Gemini + FastAPI)

An AI-powered chatbot that analyzes medical reports (PDF) and answers user queries with context-aware responses using Retrieval-Augmented Generation (RAG).

---

## Features

- Upload medical reports (PDF)
- Ask questions about your report
- Context-aware follow-up questions (chat memory)
- Accurate answers using RAG (FAISS + embeddings)
- Fast responses using Gemini API
- Source citation (page-level)
- Interactive UI with Streamlit

---

## Tech Stack

- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **LLM:** Gemini API  
- **Embeddings:** Sentence Transformers  
- **Vector DB:** FAISS  
- **PDF Parsing:** PyPDF  
- **Memory:** Sliding window chat memory  

---

## Architecture

1. User uploads PDF  
2. PDF is parsed into chunks  
3. Chunks are embedded using Sentence Transformers  
4. Stored in FAISS vector database  
5. User query → converted to embedding  
6. Top-K relevant chunks retrieved  
7. Context + memory → sent to Gemini  
8. Answer generated and returned with sources  

---

## Project Structure
