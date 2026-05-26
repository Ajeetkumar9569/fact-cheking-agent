# utils/extractor.py

import os
import pdfplumber
from groq import Groq
from dotenv import load_dotenv
from utils.prompts import CLAIM_EXTRACTION_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_text_from_pdf(pdf_path):

    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    return full_text


def extract_claims(text):

    prompt = f"""
    {CLAIM_EXTRACTION_PROMPT}

    TEXT:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    claims = result.split("\n")

    clean_claims = []

    for claim in claims:

        claim = claim.replace("-", "").replace("*", "").strip()

        # Skip unwanted intro text
        if "Here are" in claim:
            continue

        if "factual claims" in claim:
            continue

        # Remove anything inside brackets
        if "(" in claim:
            claim = claim.split("(")[0].strip()

        # Remove extra explanation after colon
        if ":" in claim:

            parts = claim.split(":")

            # Keep only first 2 parts max
            if len(parts) > 2:
                claim = parts[0] + ": " + parts[1]

        # Final cleanup
        claim = claim.strip()

        if len(claim) > 10:
            clean_claims.append(claim)

    return clean_claims