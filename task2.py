from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import chatbot function from task1
from task1 import generate_chatgpt_response

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend (React on localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Use ["*"] for all origins during dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request schema for PUT endpoint
class ChatRequest(BaseModel):
    question: str
    user: Union[str, None] = "Anonymous"

# Startup message
@app.on_event("startup")
async def startup_event():
    print("FastAPI server is running at http://127.0.0.1:8000")
    print("Swagger UI available at http://127.0.0.1:8000/docs")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API powered by LangChain + OpenAI."}

# GET-based chat endpoint (used by React frontend)
@app.get("/chat/{question}")
def get_chat_response(question: str, user: Union[str, None] = None):
    try:
        answer = generate_chatgpt_response(question)
        return {
            "user": user or "Anonymous",
            "question": question,
            "answer": answer
        }
    except Exception as e:
        return {
            "error": str(e),
            "answer": "An error occurred while processing your request."
        }

# PUT-based chat endpoint (optional, not used in React for now)
@app.put("/chat")
def put_chat_response(chat: ChatRequest):
    try:
        answer = generate_chatgpt_response(chat.question)
        return {
            "user": chat.user or "Anonymous",
            "question": chat.question,
            "answer": answer
        }
    except Exception as e:
        return {
            "error": str(e),
            "answer": "An error occurred while processing your request."
        }
