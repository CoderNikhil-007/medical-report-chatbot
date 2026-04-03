import streamlit as st
import requests

st.set_page_config(page_title="Medical Report Chatbot")

st.title("🩺 Medical Report Chatbot")

st.markdown("---")
st.info("⚠️ This is not medical advice. Please consult a doctor.")

# Upload PDF
uploaded_file = st.file_uploader("Upload your medical report (PDF)", type=["pdf"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    
    response = requests.post("http://127.0.0.1:8000/upload", files=files)
    
    if response.status_code == 200:
        st.success("File uploaded and processed successfully!")

# Ask question
query = st.text_input("Ask a question about your report")

if st.button("Get Answer"):
    if query:
        response = requests.get(
            "http://127.0.0.1:8000/query",
            params={"q": query}
        )

        if response.status_code == 200:
            data = response.json()

            st.subheader("Answer")
            st.write(data["answer"])

            st.subheader("Sources")
            st.write(data["sources"])