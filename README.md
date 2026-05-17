# RAG AI Backend

## Overview

RAG AI Backend is a Retrieval-Augmented Generation (RAG) system built using FastAPI, ChromaDB, Sentence Transformers, and Google Gemini API.

The application allows users to upload PDF documents, semantically search through their contents, and generate contextual answers using a Large Language Model (LLM).

The entire application is containerized using Docker and can be deployed locally or on cloud platforms such as Render, AWS, GCP, or Azure.

---

# Features

* Upload and process PDF documents
* Automatic text extraction and chunking
* Semantic embedding generation using Sentence Transformers
* Vector similarity search using ChromaDB
* Context-aware response generation using Gemini API
* FastAPI-based REST API
* Document metadata storage
* Dockerized deployment
* Cloud deployment support
* Swagger API documentation

---

# Tech Stack

| Technology            | Purpose                 |
| --------------------- | ----------------------- |
| FastAPI               | REST API Framework      |
| ChromaDB              | Vector Database         |
| Sentence Transformers | Text Embeddings         |
| Google Gemini API     | LLM Response Generation |
| Docker                | Containerization        |
| Python                | Backend Development     |
| SQLite                | Metadata Storage        |
| Render                | Cloud Deployment        |

---

# Project Architecture

```text
User Query
    ↓
FastAPI Backend
    ↓
Semantic Retrieval (ChromaDB)
    ↓
Relevant Document Chunks
    ↓
Gemini LLM
    ↓
Contextual AI Response
```

---

# Project Structure

```text
RAG_Project/
│
├── app/
│   └── utils/
│       ├── database.py
│       ├── embedding_generator.py
│       ├── llm_generator.py
│       ├── pdf_reader.py
│       ├── text_chunker.py
│       └── vector_store.py
│
├── uploads/
├── chroma_db/
├── tests/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

---

# API Endpoints

## 1. Upload PDF

### Endpoint

```http
POST /upload
```

### Description

Uploads and processes PDF documents.

### Features

* PDF validation
* Text extraction
* Chunk generation
* Embedding creation
* Vector database storage
* Metadata storage

---

## 2. Query System

### Endpoint

```http
POST /query
```

### Description

Accepts user questions and retrieves relevant chunks from uploaded documents before generating a contextual answer using Gemini.

### Example Request

```json
{
  "question": "What are the evaluation criteria?"
}
```

---

## 3. View Documents

### Endpoint

```http
GET /documents
```

### Description

Returns metadata for all processed documents.

---

# Local Installation Setup

## 1. Clone Repository

```bash
git clone https://github.com/krishnagupta7171/rag-ai.git

cd rag-ai
```

---

## 2. Create Virtual Environment

```bash
python -m venv rag_env
```

---

## 3. Activate Virtual Environment

### Windows

```bash
rag_env\Scripts\activate
```

### Linux / Mac

```bash
source rag_env/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

# Run Application Locally

```bash
uvicorn main:app --reload
```

---

# Swagger API Documentation

After starting the server:

```text
http://127.0.0.1:8000/docs
```

---

# Docker Deployment

## Build Docker Container

```bash
docker compose build
```

---

## Run Docker Container

```bash
docker compose up
```

---

# Render Cloud Deployment

This project supports deployment on Render using Docker.

## Deployment Steps

1. Push project to GitHub
2. Create Web Service on Render
3. Select Docker environment
4. Add environment variable:

```env
GEMINI_API_KEY=your_gemini_api_key
```

5. Deploy application

---

# Live Deployment

```text
Add your Render deployment URL here
```

Example:

```text
https://rag-ai.onrender.com/docs
```

---

