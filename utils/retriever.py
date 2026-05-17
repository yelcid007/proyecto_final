import chromadb
from sentence_transformers import SentenceTransformer


# Modelo de embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_store(chunks, embeddings):
    """
    Crea y guarda la base vectorial.
    """

    # Cliente persistente
    client = chromadb.PersistentClient(path="chroma_db")

    # Crear colección
    collection = client.get_or_create_collection(
        name="reglamento_collection"
    )

    # Agregar documentos
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embedding.tolist()]
        )

    print("\nBase vectorial creada correctamente.\n")


def search_context(query, top_k=3):
    """
    Busca contexto relevante usando similitud semántica.
    """

    # Cliente persistente
    client = chromadb.PersistentClient(path="chroma_db")

    # Abrir colección existente
    collection = client.get_collection(
        name="reglamento_collection"
    )

    # Embedding de la pregunta
    query_embedding = model.encode(query).tolist()

    # Buscar similitud
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "distances"]
    )

    return results