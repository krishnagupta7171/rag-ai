from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_rag_response(question, retrieved_chunks):

    # Combine retrieved chunks
    context = "\n\n".join(retrieved_chunks)

    # Prompt
    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the provided context.

If the answer is not present in the context, say:
"I could not find the answer in the uploaded documents."

Context:
{context}

Question:
{question}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return str(e)