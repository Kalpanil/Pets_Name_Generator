
from langchain_ollama import OllamaLLM

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


llm= OllamaLLM(model="llama3.2",temperature=0.2)

def langchain_agent():
    llm= OllamaLLM(model="llama3.2",temperature=0.2)

    tools=load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose =True
    )

    result= agent.run("What is the average age of the Dog? Multiply th age by 3")
    print(result)

def generate_pet_name(animal_types, pet_color):
    prompt_template_name=PromptTemplate(
        input_variables=['animal_types','pet_color'],
        template ="I have a {animal_types} & i want a cool name for it, it is {pet_color}in color. suggest me five cool names foy my pet. only provide the names"
         )
    
    name_chain = prompt_template_name | llm

    response= name_chain.invoke({'animal_types':animal_types, 'pet_color' : pet_color })
    return response


if __name__ =="__main__":
    langchain_agent()
    # print(generate_pet_name("Dog", "White"))