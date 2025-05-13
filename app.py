from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Streamlit UI
st.title("Chatbot")
input_text = st.text_input("Ask me anything:")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's queries."),
    ("user", "Question: {question}")
])

# Use Ollama model (make sure Ollama is running Mistral)
llm = ChatOllama(model="mistral")  # You can change to "llama2", "gemma", etc.

# Output parser
output_parser = StrOutputParser()

# Create chain
chain = prompt | llm | output_parser

# Chat handling
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
