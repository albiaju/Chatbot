import os
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize the language model
chat = ChatOpenAI(
    temperature=0,
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Set up conversation memory
memory = ConversationEntityMemory(llm=chat, k=10)

# Create a ConversationChain with memory
conversation = ConversationChain(
    llm=chat,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=memory,
    verbose=False
)

def generate_chatgpt_response(question: str) -> str:
    try:
        return conversation.run(question).strip()
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
