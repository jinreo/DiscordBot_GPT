#chatgpt.py
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
client = OpenAI(api_key=OPENAI_KEY)


def send_to_chatGpt(messages, model="gpt-4o"):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message