from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


from task1 import generate_chatgpt_response

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
    return {"message": "Welcome to the Chatbot API powered by LangChain + OpenAI."}

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
