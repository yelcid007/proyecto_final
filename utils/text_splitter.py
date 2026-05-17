import re


def split_text_into_chunks(text):
    """
    Divide el texto por artículos.
    """

    # Detectar artículos
    pattern = r"(Artículo\s+\d+[\s\S]*?)(?=Artículo\s+\d+|$)"

    matches = re.findall(pattern, text, re.IGNORECASE)

    chunks = []

    for match in matches:

        cleaned = match.strip()

        if len(cleaned) > 100:
            chunks.append(cleaned)

    return chunks