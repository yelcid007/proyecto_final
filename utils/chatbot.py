import ollama

from utils.prompt import SYSTEM_PROMPT
from utils.retriever import search_context


def generate_response(user_question):
    """
    Genera respuesta usando RAG + Ollama.
    """

    # Buscar contexto
    results = search_context(user_question)

    documents = results["documents"][0]

    distances = results["distances"][0]

    # Verificar relevancia semántica
    best_distance = distances[0]

    print(f"\nDistancia semántica: {best_distance}\n")

    # Si la distancia es muy alta,
    # significa que no encontró contexto relevante
    if best_distance > 1.03:

        print("\n[INFO] Consulta fuera del dominio del reglamento.\n")

        return "No encuentro esa información en el reglamento.", []

    # Unir contexto
    context = "\n\n".join(documents)

    # Prompt aumentado
    final_prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO:
{context}

PREGUNTA:
{user_question}
"""

    # Generar respuesta
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    answer = response["message"]["content"]

    return answer, documents