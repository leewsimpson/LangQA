from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
ai = ChatOpenAI()

chat = [
    SystemMessage(content="You are a grump bot, and you always try to annoy the user.")
]

while True:

    Input = input("You: ")
    chat.append(HumanMessage(content=Input))    
    response = ai(chat)
    print("Bot: " + response.content)
    chat.append(AIMessage(content=response.content))


