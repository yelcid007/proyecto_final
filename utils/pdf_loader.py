import os
import re
from pypdf import PdfReader


def clean_text(text):
    """
    Limpia texto extraído del PDF.
    """

    # Eliminar saltos múltiples
    text = re.sub(r'\n+', '\n', text)

    # Eliminar espacios múltiples
    text = re.sub(r'\s+', ' ', text)

    # Corregir espacios antes de saltos
    text = text.strip()

    return text


def load_pdfs_from_folder(folder_path):
    """
    Lee todos los PDFs de una carpeta
    y devuelve el texto limpio.
    """

    full_text = ""

    for filename in os.listdir(folder_path):

        if filename.endswith(".pdf"):

            pdf_path = os.path.join(folder_path, filename)

            print(f"Leyendo: {filename}")

            reader = PdfReader(pdf_path)

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    cleaned = clean_text(text)

                    full_text += cleaned + "\n"

    return full_text