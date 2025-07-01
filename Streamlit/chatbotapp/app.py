from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os




def ai_response(user_msg):
    load_dotenv()
    cohere_key = os.getenv("COHERE_API_KEY")
    llm = Cohere(cohere_api_key = cohere_key)


    template = "{user_msg}"
    prompt = PromptTemplate.from_template(template)


    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(user_msg)
    return response

