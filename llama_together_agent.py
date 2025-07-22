import os
import openai
from dotenv import load_dotenv
from openfda_api import extract_fda_info


load_dotenv(encoding="utf-16")

api_key = os.environ.get("TOGETHER_API_KEY")
base_url = "https://api.together.xyz/v1"

client = openai.OpenAI(
    api_key = api_key,
    base_url = base_url
)

def medical_chatbot(user_input):
     # If user asks "suggest a drug for X", let LLaMA handle it directly
    suggest_keywords = ["suggest", "recommend", "give me a drug", "what should I take", "medicine for"]
    if any(kw in user_input.lower() for kw in suggest_keywords):
        prompt = f"""
                You are a helpful medical assistant. A user asked: "{user_input}"

                Answer with a commonly used over-the-counter or prescription medicine, with a short explanation.
                Avoid brand recommendations unless commonly known.
"""
         
        response = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[
            {
                "role": "user",
                "content": prompt
            }
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    # Else treat input as a drug name query
    words = user_input.lower().split()
    drug_name = words[-1] if len(words) > 0 else "aspirin"

    fda_info = extract_fda_info(drug_name)
    if not fda_info:
        return "Sorry, I couldn't find information on that drug."


    # Build prompt with usage, warnings, reactions
    prompt = f"""
    You are a helpful medical assistant.
    User asked: {user_input}

    Here is FDA drug label information:
    - Usage: {fda_info['usage']}
    - Warnings: {fda_info['warnings']}
    - Adverse Reactions: {fda_info['reactions']}

    Please summarize all this clearly and concisely for a general audience.
    """

    response = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[
    {
        "role": "user",
        "content": prompt
    }
    ],
    temperature=0.7
    )
    return response.choices[0].message.content