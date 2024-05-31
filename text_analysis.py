from dotenv import load_dotenv
import os

load_dotenv()

#print("loaded API Key:", os.getenv("OPENAI_API_KEY"))

from openai import OpenAI

# Initialize OpenAI client
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI()

def analyze_transcript(transcript: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful cybersecurity expert. Your task is to analyze the text and provide direct answers to any questions posed in the transcript. Your outputs should be succinct and provide clear, informative answers."},
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content
