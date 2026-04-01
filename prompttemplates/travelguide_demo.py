from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from basics import streamlit as st

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
pt=PromptTemplate(input_variables=["city","days","language","budget"],
                  template="""
                  Welcome to {city} Travel Guide!
                  Make a {days} days wise plan to travel
                  1. Visit the famous locations.
                  2. Local cuisine you must try.
                  3. Useful phrases in {language}.
                  4. Tips for travelling on a {budget} budget.
                  
                  If the {city} city is fictional and non-existent. So, Answer this and exit from city if fictional.
                  Answer: I don't about {city}. Maybe it doesn't exist.
                  Enjoy your trip:)
                  """)

st.title("haveTravel")
city=st.text_input("Enter the city")
days=st.text_input("Enter the days")
language=st.text_input("Enter the language")
budget=st.selectbox("Enter the budget",["Low","Medium","High"])
if st.button("Generate plan"):
    st.write("Generating your plan...")
    # llm.generate_plan(city,days,language,budget)

if city and days and language and budget:
    response=llm.invoke(pt.format(city=city, days=days, language=language, budget=budget))
    st.write(response.content)
