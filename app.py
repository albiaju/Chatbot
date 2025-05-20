from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load the OpenAI API key safely
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class ChatRequest(BaseModel):
    question: str
    user: Union[str, None] = "Anonymous"

@app.on_event("startup")
async def startup_event():
    print("FastAPI server is running at http://127.0.0.1:8000")
    print("Swagger UI available at http://127.0.0.1:8000/docs")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API powered by ChatGPT 3.5-turbo."}

@app.get("/chat/{question}")
def get_chat_response(question: str, user: Union[str, None] = None):
    answer = generate_chatgpt_response(question)
    return {
        "user": user or "Anonymous",
        "question": question,
        "answer": answer
    }

@app.put("/chat")
def put_chat_response(chat: ChatRequest):
    answer = generate_chatgpt_response(chat.question)
    return {
        "user": chat.user or "Anonymous",
        "question": chat.question,
        "answer": answer
    }
def generate_chatgpt_response(question: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=150,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {e}"





