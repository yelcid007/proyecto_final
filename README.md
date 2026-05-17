# Proyecto Final — Sistema RAG para Consulta de Reglamento Académico

<img width="1907" height="1025" alt="image" src="https://github.com/user-attachments/assets/6776faf5-4f4f-45b5-9fc5-aa533505e2c9" />


## Descripción del Proyecto

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) capaz de responder preguntas relacionadas con un reglamento académico institucional utilizando búsqueda semántica, embeddings y modelos de lenguaje.

El sistema permite consultar información del reglamento de manera inteligente mediante una interfaz gráfica amigable, evitando alucinaciones y respondiendo únicamente con información contenida en los documentos cargados.

---

# Objetivos

* Implementar un sistema RAG funcional.
* Realizar búsqueda semántica sobre documentos PDF.
* Utilizar embeddings para representar información textual.
* Persistir información en una base vectorial.
* Generar respuestas contextualizadas usando un LLM.
* Evitar respuestas inventadas o fuera del dominio.
* Crear una interfaz gráfica funcional para interacción con el usuario.

---

# Tecnologías Utilizadas

| Tecnología              | Uso                         |
| ----------------------- | --------------------------- |
| Python                  | Desarrollo principal        |
| Streamlit               | Interfaz gráfica            |
| ChromaDB                | Base de datos vectorial     |
| SentenceTransformers    | Generación de embeddings    |
| Ollama + Llama 3.2      | Modelo de lenguaje local    |
| PyPDF                   | Extracción de texto PDF     |
| LangChain Text Splitter | División semántica de texto |

---

# Arquitectura del Sistema

```text
Usuario
   ↓
GUI Streamlit
   ↓
Consulta del usuario
   ↓
Embeddings de la consulta
   ↓
Búsqueda semántica en ChromaDB
   ↓
Recuperación de chunks relevantes
   ↓
Construcción del Prompt Aumentado
   ↓
LLM (Llama 3.2 vía Ollama)
   ↓
Respuesta final
```

---

# Flujo General del Sistema

## 1. Ingesta de Documentos

Los documentos PDF del reglamento son cargados desde la carpeta:

```text
/data
```

El sistema extrae automáticamente el texto de cada documento.

---

## 2. División Semántica

El texto completo se divide en fragmentos llamados chunks utilizando:

```python
RecursiveCharacterTextSplitter
```

Esto mejora:

* precisión semántica
* recuperación contextual
* rendimiento del embedding

---

## 3. Vectorización

Cada chunk es convertido a embeddings utilizando el modelo:

```text
all-MiniLM-L6-v2
```

### Justificación del Modelo

Se eligió este modelo porque:

* funciona localmente
* es liviano y eficiente
* posee buen soporte multilingüe
* tiene excelente rendimiento semántico
* permite procesamiento rápido sin GPU

### Características

| Característica  | Valor                |
| --------------- | -------------------- |
| Dimensiones     | 384                  |
| Tipo            | Sentence Transformer |
| Ejecución local | Sí                   |
| Soporte español | Sí                   |

---

# Base Vectorial

Se utilizó:

```text
ChromaDB
```

para almacenar:

* embeddings
* chunks
* metadatos

La información queda persistida localmente en:

```text
/chroma_db
```

---

# Recuperación Semántica

Cuando el usuario realiza una pregunta:

1. Se genera el embedding de la consulta.
2. Se calcula similitud semántica.
3. Se recuperan los chunks más cercanos.

El sistema permite recuperar información incluso usando:

* lenguaje coloquial
* sinónimos
* preguntas indirectas

## Ejemplo

Pregunta:

```text
¿Qué pasa si pierdo materias?
```

Recuperación encontrada:

```text
Cancelación por bajo rendimiento académico
```

---

# Construcción del Prompt Aumentado

El sistema construye dinámicamente un prompt con:

* instrucciones del sistema
* contexto recuperado
* pregunta del usuario

## Prompt Base

```text
Responde únicamente usando la información del contexto.
Si no encuentras información suficiente responde:
"No encuentro esa información en el reglamento."
```

---

# Prevención de Alucinaciones

Para evitar respuestas inventadas se implementaron:

## 1. Restricción del Prompt

El modelo solo puede responder utilizando contexto recuperado.

---

## 2. Threshold Semántico

Se implementó validación por distancia semántica.

Si la consulta está fuera del dominio del reglamento:

```text
No encuentro esa información en el reglamento.
```

---

# Modelo de Lenguaje

El sistema utiliza:

```text
Llama 3.2
```

ejecutado localmente mediante:

```text
Ollama
```

Ventajas:

* ejecución local
* privacidad
* rapidez
* sin costos API

---

# Interfaz Gráfica

La GUI fue desarrollada con:

```text
Streamlit
```

Características:

* caja de consulta
* visualización de respuestas
* visualización de fuentes
* interfaz amigable
* funcionamiento local

---

# Estructura del Proyecto

```text
PROYECTO_FINAL/

│
├── app.py
├── ingest.py
├── test_chatbot.py
├── requirements.txt
│
├── data/
│
├── chroma_db/
│
├── utils/
│   ├── chatbot.py
│   ├── embeddings.py
│   ├── pdf_loader.py
│   ├── prompt.py
│   ├── retriever.py
│   └── text_splitter.py
```

---

# Instalación del Proyecto

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2. Crear entorno virtual

```bash
python -m venv venv
```

---

## 3. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Construcción de la Base Vectorial

Ejecutar:

```bash
python ingest.py
```

Esto:

* procesa PDFs
* genera embeddings
* crea la base vectorial

---

# Ejecución de la Aplicación

```bash
streamlit run app.py
```

---

# Evaluación del Sistema

Se realizaron pruebas utilizando preguntas válidas y preguntas fuera del dominio.

---

# Resultados de Evaluación

| Pregunta                          | Resultado |
| --------------------------------- | --------- |
| ¿Qué pasa si pierdo materias?     | Correcto  |
| ¿Puedo repetir una asignatura?    | Correcto  |
| ¿Qué necesito para graduarme?     | Correcto  |
| ¿Qué son las pruebas supletorias? | Correcto  |
| ¿Cómo cancelar una materia?       | Correcto  |
| ¿Qué pasa por bajo rendimiento?   | Correcto  |
| ¿Cómo hacer arroz con pollo?      | Bloqueado |
| ¿Quién ganó el mundial?           | Bloqueado |
| ¿Cuál es la capital de Francia?   | Bloqueado |
| ¿Cómo programar en Python?        | Bloqueado |

---

# Análisis de Resultados

## Caso Exitoso

Pregunta:

```text
¿Qué pasa si pierdo varias materias?
```

Resultado:

* recuperación correcta
* respuesta contextualizada
* alta relevancia semántica

---

## Caso de Error

Pregunta:

```text
¿Puedo recuperar materias?
```

Problema:

* el reglamento utilizaba términos diferentes
* la recuperación inicial no encontró suficiente similitud

Solución:

* ajuste del threshold semántico
* mejora del prompt contextual

---

# Conclusiones

El sistema logró implementar exitosamente:

* búsqueda semántica
* embeddings
* recuperación contextual
* base vectorial persistente
* generación aumentada por recuperación
* control anti-alucinaciones
* interfaz gráfica funcional

El proyecto demuestra cómo construir asistentes especializados utilizando IA generativa y recuperación semántica de documentos institucionales.

---

# Autor

Camilo Leyton

Proyecto Final — Sistema RAG Académico
2026
