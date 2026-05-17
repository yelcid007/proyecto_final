from utils.chatbot import generate_response


print("\n===== CHATBOT RAG =====\n")


question = input("Haz una pregunta: ")


response, sources = generate_response(question)


print("\n===== RESPUESTA =====\n")

print(response)


# Mostrar fuentes solo si existen
if len(sources) > 0:

    print("\n===== FUENTES =====\n")

    for i, source in enumerate(sources):

        print(f"\n--- Fuente {i+1} ---\n")

        print(source)