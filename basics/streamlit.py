import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Enabled debug in LangChain -> explain overall about how it works
from langchain_core.globals import set_debug
set_debug(True)

# Main code
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.title("AskQuery")
query=st.text_input("Ask your question here... ")

if query:
    response=llm.invoke(query)
    st.write(response.content)