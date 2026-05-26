# utils/extractor.py

import re
import pdfplumber


def extract_text_from_pdf(pdf_path):

    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    return full_text


def extract_claims(text):

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    clean_claims = []

    for sentence in sentences:

        sentence = sentence.strip()

        # Remove bullets
        sentence = sentence.replace("•", "")
        sentence = sentence.replace("-", "")
        sentence = sentence.replace("*", "")

        # Remove extra spaces
        sentence = sentence.strip()

        # Skip empty or tiny lines
        if len(sentence) < 5:
            continue

        # Avoid duplicates
        if sentence not in clean_claims:
            clean_claims.append(sentence)

    return clean_claims