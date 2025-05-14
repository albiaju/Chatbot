import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()

def run_chat():
    chat = ChatOpenAI(
        temperature=0.7,
        model="gpt-4o",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat.invoke([HumanMessage(content=user_input)])
        print("Bot:", response.content)

run_chat()
