from sentence_transformers import SentenceTransformer


# Cargar modelo una sola vez
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks):
    """
    Genera embeddings para cada chunk.
    """

    embeddings = model.encode(chunks)

    return embeddings