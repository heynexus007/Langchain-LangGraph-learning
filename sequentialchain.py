from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

# Sequential Chain
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
title_prompt = PromptTemplate(input_variables=["topic"],
                              template="""
                              You are an experienced speech writer.
                              You need to craft an impactful title for a speech on the following topics: {topic}
                              Answers exactly with one title.
                              """)

speech_prompt = PromptTemplate(input_variables=["title","emotion"],
                               template="""
                               You need to write a {emotion} professional speech of 350 words
                               for the following title: {title}
                               """)

chain1 = title_prompt | llm | StrOutputParser() | (lambda title: (st.write(title),title)[1])
chain2 = speech_prompt | llm
final_chain = chain1 | (lambda title: {"title":title, "emotion": emotion}) | chain2

st.title("Speech Generator")
topic=st.text_input("Enter the topic here...")
emotion=st.text_input("Enter the emotion here...")

if st.button("Generate speech"):
    st.write("Generating speech...")

    if topic:
        response = final_chain.invoke({"topic": topic})
        st.write(response.content)