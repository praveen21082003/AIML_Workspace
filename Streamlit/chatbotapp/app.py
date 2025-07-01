from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_cohere import ChatCohere


load_dotenv()
cohere_key = os.getenv("COHERE_API_KEY")

def get_current_temperature(location: str) -> float:
    """Used to get current temperature in a given location."""
    return 53.3


def ai_response(user_msg):
    
    llm = ChatCohere(cohere_api_key = cohere_key)
    template = "Answer the user question briefly - {user_msg}"
    prompt = PromptTemplate.from_template(template)

    chain = prompt | llm.bind_tools([get_current_temperature]) 

    response = chain.invoke({"user_msg": user_msg}).content
    return response


