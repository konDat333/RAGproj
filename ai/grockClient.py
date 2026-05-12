import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



def get_response(message: str) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant to help the user search the web for information."},
             {"role": "user",
             "content": message}
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

print(get_response("What is the capital of France?"))