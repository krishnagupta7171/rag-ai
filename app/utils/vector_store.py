import chromadb


client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="rag_collection"
)


def store_embeddings(chunks, embeddings):

    ids = []

    for i in range(len(chunks)):
        ids.append(f"chunk_{i}")

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    return len(ids)

def search_similar_chunks(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results