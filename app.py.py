import streamlit as st
# from langchain_ollama import Ollama
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
# Initialize the LLM
llm = OllamaLLM(model="llama3.2", temperature=0.2)

def generate_pet_name(animal_types, pet_color):
    """Generates pet names based on animal type and color."""
    prompt_template_name = PromptTemplate(
        input_variables=['animal_types', 'pet_color'],
        template="I have a {animal_types} & I want a cool name for it. It is {pet_color} in color. Suggest me five cool names for my pet. Only provide the names."
    )

    # Used RunnableSequence (prompt → LLM)
    name_chain = prompt_template_name | llm
    response = name_chain.invoke({'animal_types': animal_types, 'pet_color': pet_color})

    
    return response.strip().split("\n")

# Streamlit UI
st.title("Pet Name Generator")

# Sidebar for user input
st.sidebar.header("Select Your Pet")
animal_types = st.sidebar.selectbox("Choose Pet Type", ["Dog", "Cat", "Bird", "Rabbit", "Horse", "Fish", "Turtle", "Other"])
pet_color = st.sidebar.text_input("Enter Pet Color", placeholder="e.g., White, Brown, Golden")


if st.sidebar.button("Generate Names"):
    if animal_types and pet_color:
        names = generate_pet_name(animal_types, pet_color)
        st.success(f"Here are five cool names for your {pet_color} {animal_types}:")
        for i, name in enumerate(names, 1):
            st.write(f"**{name}**")
    else:
        st.warning("Please enter both pet type and color!")



