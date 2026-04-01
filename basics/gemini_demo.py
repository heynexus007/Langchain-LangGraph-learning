import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash") #, GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
chat_history=[]
print("Chatbot is ready!! Type 'exit' to stop")
while True:
    user_input = input("You: ")
    if user_input in ["exit", "quit"]:
        print("Goodbye!")
        break
    chat_history.append(HumanMessage(content=user_input))
    response=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))

    print("Chatbot responses: ", response.content)

