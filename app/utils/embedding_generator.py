from sentence_transformers import SentenceTransformer

model = None

def load_model():

    global model

    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")

    return model


def generate_embeddings(chunks):

    current_model = load_model()

    embeddings = current_model.encode(chunks)

    return embeddings