from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

ai = OpenAI()

prompt = PromptTemplate(template="hello, my name is {name}", input_variables=["name"])

chain = LLMChain(llm=ai, prompt=prompt)
print(chain.run("Lee"))
