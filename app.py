import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from config.models.llm import generate_response
from utils.rag import create_vector_db, retrieve_docs
from utils.web_search import search_web

st.set_page_config(page_title="Career Chatbot", layout="wide")

st.title("🎯 AI Career Assistant Chatbot")

# Status indicator
st.info("🖥️ Running in Local AI Mode (no OpenAI required)")

mode = st.radio("Choose Response Mode", ["Concise", "Detailed"])

query = st.text_input("Ask your career question:")

@st.cache_resource
def load_db():
    return create_vector_db()

db = load_db()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

col1, col2 = st.columns(2)

with col1:
    if st.button("Get Answer"):
        if query:
            docs = retrieve_docs(query, db)
            context = " ".join([doc.page_content for doc in docs])

            if mode == "Concise":
                prompt = f"Give a short answer: {query} using context: {context}"
            else:
                prompt = f"Give a detailed explanation: {query} using context: {context}"

            response = generate_response(prompt)

            # safer string check
            if "don't know" in response.lower() or "not sure" in response.lower():
                web_result = search_web(query)
                response += f"\n\n🌐 Web Data: {web_result}"

            # Add to history
            st.session_state.chat_history.append({"query": query, "response": response})

            st.success(response)
        else:
            st.warning("Please enter a question")

with col2:
    if st.button("Clear History"):
        st.session_state.chat_history = []
        st.success("Chat history cleared!")

# Display chat history
if st.session_state.chat_history:
    st.subheader("Chat History")
    for i, chat in enumerate(st.session_state.chat_history):
        st.write(f"**Q{i+1}:** {chat['query']}")
        st.write(f"**A{i+1}:** {chat['response']}")
        st.write("---")