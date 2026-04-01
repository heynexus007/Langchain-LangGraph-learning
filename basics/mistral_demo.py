import os
from langchain_community.chat_models import ChatOllama

llm=ChatOllama(model="mistral")
query=input("Ask your question: ")
response=llm.invoke(query)
print("AI Answer: ", response.content)