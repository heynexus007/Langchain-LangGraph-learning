from basics import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Enabled debug in LangChain -> explain overall about how it works
from langchain_core.globals import set_debug
set_debug(True)

# Main code
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# For Multiple input variables
# pt = PromptTemplate(input_variables=["country", "no_of_paragraphs", "language"],
#                     template=""""
#                     """)
pt=PromptTemplate(input_variables=["country"],
                  template=""""
                  You are expert in traditional cuisine.
                  So, Provide me information about Top five traditional Dishes in specific country 
                  and also provide how it is made in short.
                  Avoid giving information about fictional places. If the country is fictional or not exist. Answer: Sorry! I don't know about this {country}.
                  Answers the question: What is the traditional dishes based on {country} and steps to make that cuisine.
                  """)
st.title("Welcome to CuisineVerse")
country=st.text_input("Enter the country")

if country:
    response=llm.invoke(pt.format(country=country))
    st.write(response.content)