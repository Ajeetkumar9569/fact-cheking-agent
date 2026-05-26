# utils/verifier.py

import os
from duckduckgo_search import DDGS
from groq import Groq
from dotenv import load_dotenv
from utils.prompts import VERIFICATION_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def search_web(query):

    results = []

    with DDGS() as ddgs:

        search_results = ddgs.text(query, max_results=5)

        for r in search_results:

            if "body" in r:
                results.append(r["body"])

    return " ".join(results)


def verify_claim(claim):

    web_data = search_web(claim)

    prompt = f"""
    Claim:
    {claim}

    Web Data:
    {web_data}

    {VERIFICATION_PROMPT}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    status = "Unknown"
    info = "No additional information found."

    lines = result.split("\n")

    for line in lines:

        line = line.strip()

        # ---------- STATUS ----------

        if "Status:" in line:

            extracted_status = line.replace("Status:", "").strip().lower()

            if "verified" in extracted_status:
                status = "VERIFIED"

            elif "inaccurate" in extracted_status:
                status = "INACCURATE"

            elif "false" in extracted_status:
                status = "FALSE"

        # ---------- CORRECT INFO ----------

        if "Correct Info:" in line:

            extracted_info = line.replace("Correct Info:", "").strip()

            if extracted_info:
                info = extracted_info

    # ---------- EXTRA SAFETY CHECK ----------

    if "not" in info.lower():
        status = "INACCURATE"

    if "incorrect" in info.lower():
        status = "INACCURATE"

    if "false" in info.lower():
        status = "FALSE"

    return status, info