from utils.retriever import search_context


print("\n===== PRUEBA DE BÚSQUEDA SEMÁNTICA =====\n")


# Pregunta del usuario
query = input("Haz una pregunta: ")


# Buscar contexto
results = search_context(query)


# Obtener documentos recuperados
documents = results["documents"][0]


# Mostrar resultados
for i, doc in enumerate(documents):

    print(f"\n========== RESULTADO {i+1} ==========\n")

    print(doc)