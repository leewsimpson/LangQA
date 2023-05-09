from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import random

def random_num(input=""):
    max=int(input)
    return random.randint(0, max)

random_tool = Tool(
    name="Random Number",
    func=random_num,
    description="Useful for when you need to get a random number. Input is the maximum number to generate.",
)

llm = OpenAI(temperature=0)
tools = [random_tool]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print(agent.run("What is a number between 1 and 5?"))