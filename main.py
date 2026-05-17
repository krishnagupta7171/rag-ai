
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File
from app.utils.pdf_reader import extract_text_from_pdf
from app.utils.text_chunker import chunk_text
from app.utils.llm_generator import generate_rag_response
from app.utils.embedding_generator import generate_embeddings
from app.utils.vector_store import store_embeddings, search_similar_chunks
from app.utils.database import (
    save_document_metadata,
    get_all_documents
)
from datetime import datetime
import shutil
import os

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "message": "RAG Backend Running Successfully"
    }


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    
    if not file.filename.endswith(".pdf"):
        return {
            "error": "Only PDF files are allowed"
        }

    
    file_path = os.path.join("uploads", file.filename)

    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    extracted_text = extract_text_from_pdf(file_path)
    chunks = chunk_text(extracted_text)
    embeddings = generate_embeddings(chunks)
    stored_count = store_embeddings(chunks, embeddings)
    upload_time = str(datetime.now())

    save_document_metadata(
        file.filename,
        upload_time,
        len(chunks)
    )
    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename,
        "total_chunks": len(chunks),
        "embedding_dimension": len(embeddings[0]),
        "stored_count": stored_count
    }

@app.post("/query")
def query_rag(request: QueryRequest):

    
    question = request.question

    question_embedding = generate_embeddings([question])[0]

    results = search_similar_chunks(question_embedding)

    retrieved_chunks = results["documents"][0]

    final_answer = generate_rag_response(
        question,
        retrieved_chunks
    )

    return {
        "question": question,
        "answer": final_answer,
        "retrieved_chunks": retrieved_chunks
    }

@app.get("/documents")
def get_documents():

    documents = get_all_documents()

    return {
        "documents": documents
    }