import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_gemini(question, deals, work_orders):

    prompt = f"""
You are NovaBI, an AI Business Intelligence Assistant.

You must answer ONLY using the business data below.

Deals Data:
{deals.head(50).to_string()}

Work Orders Data:
{work_orders.head(50).to_string()}

User Question:
{question}

Rules:
- Never say you are Gemini.
- Say you are NovaBI.
- Base every answer on the provided business data.
- If the answer cannot be found in the data, politely say:
  "I couldn't find that information in the current business data."
- Keep answers professional and concise.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text