chat_history = []

def add_to_memory(question, answer):
    chat_history.append({
        "question": question,
        "answer": answer
    })

def get_memory(limit=4): 
    return chat_history[-limit:]