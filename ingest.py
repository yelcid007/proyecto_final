from utils.pdf_loader import load_pdfs_from_folder
from utils.text_splitter import split_text_into_chunks
from utils.embeddings import generate_embeddings
from utils.retriever import create_vector_store


# Ruta de PDFs
DATA_PATH = "data"


print("\nCargando PDFs...\n")

# Cargar PDFs
text = load_pdfs_from_folder(DATA_PATH)


print("\nDividiendo texto en chunks...\n")

# Crear chunks
chunks = split_text_into_chunks(text)


print(f"Cantidad de chunks: {len(chunks)}")


print("\nGenerando embeddings...\n")

# Generar embeddings
embeddings = generate_embeddings(chunks)


print("\nCreando base vectorial...\n")

# Crear vector store
create_vector_store(chunks, embeddings)


print("\nProceso finalizado correctamente.\n")