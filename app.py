import streamlit as st

from utils.chatbot import generate_response


st.set_page_config(
    page_title="Chatbot Reglamento",
    page_icon="📘",
    layout="centered"
)


st.title("📘 Chatbot Reglamento Académico")

st.markdown(
    "Haz preguntas relacionadas con el reglamento institucional."
)


question = st.text_input(
    "Escribe tu pregunta:"
)


if st.button("Consultar"):

    if question.strip() != "":

        with st.spinner("Buscando respuesta..."):

            response, sources = generate_response(question)

        st.subheader("Respuesta")

        st.write(response)

        # Mostrar fuentes si existen
        if len(sources) > 0:

            st.subheader("Fuentes consultadas")

            for i, source in enumerate(sources):

                with st.expander(f"Fuente {i+1}"):

                    st.write(source)