import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()


chat = ChatOpenAI(
    temperature=0,
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_chatgpt_response(question: str) -> str:
    try:
        response = chat.invoke([HumanMessage(content=question)])
        return response.content.strip()
    except Exception as e:
        return f"Error generating response: {e}"

if __name__ == "__main__":
    print("Chat with the bot! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = generate_chatgpt_response(user_input)
        print("Bot:", answer)