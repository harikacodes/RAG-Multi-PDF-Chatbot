import streamlit as st
from utils.pdf_reader import extract_text_from_pdfs
from utils.text_chunker import get_text_chunks
from utils.vector_store import get_vector_store
from utils.chatbot import get_answer

st.set_page_config(page_title="RAG Multi-PDF Chatbot")

st.title("📚 RAG Multi-PDF Chatbot")

pdf_docs = st.file_uploader(
    "Upload your PDF files",
    accept_multiple_files=True,
    type="pdf"
)

if pdf_docs:

    raw_text = extract_text_from_pdfs(pdf_docs)

    chunks = get_text_chunks(raw_text)

    st.subheader("Text Chunking Results")

    st.success(f"Total Chunks Created: {len(chunks)}")

    if st.button("Create Vector Database"):

        get_vector_store(chunks)

        st.success("FAISS Vector Database Created Successfully!")

st.subheader("Ask Questions")

user_question = st.text_input(
    "Ask a question about the uploaded PDFs"
)

if st.button("Get Answer"):

    answer = get_answer(user_question)

    st.subheader("AI Answer")

    st.write(answer)