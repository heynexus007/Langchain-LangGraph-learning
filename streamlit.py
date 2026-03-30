import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.title("AskQuery")
query=st.text_input("Ask your question here... ")

if query:
    response=llm.invoke(query)
    st.write(response.content)