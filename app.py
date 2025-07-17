import streamlit as st
from llama_together_agent import medical_chatbot

st.set_page_config(page_title="Medical Assistant Bot", page_icon="💊")
st.title("💊 Medical Information Assistant")

query = st.text_input("Ask a question about a drug (e.g., 'What are the side effects of aspirin?')")

if query:
    with st.spinner("Thinking..."):
        response = medical_chatbot(query)
        st.success(response)
