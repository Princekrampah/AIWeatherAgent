from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.utilities.dataforseo_api_search import DataForSeoAPIWrapper
from decouple import config
import os

os.environ["DATAFORSEO_LOGIN"] = config("DATAFORSEO_LOGIN")
os.environ["DATAFORSEO_PASSWORD"] = config("DATAFORSEO_PASSWORD")

model = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"))

prompt = ChatPromptTemplate.from_template(
    """Your are a very friendly and charming AI assistant. Help answer \
        the user questions in a friendly and funny tone. Use the provided context to answer the user question.\
        your response should be in the language specified. Below are a list of traits\ 
        you should demostrate in your response
        
    traints: {traits}
        
    Language: {language}
    
    Human: {question}
    
    Context: {context}
    
    AI:""")

chain = prompt | model | StrOutputParser()


def generate_ai_reponse(
        language: str,
        traits: list,
        user_prompt: str) -> str:
    """
    Takes in prompt and generates a response based on the context

    :user_prompt: String of the user prompt
    :traits: List of traits the bot should uphold
    :param: Language: A string of the language the user want to use

    :returns: A dictionary of the context and a string of the AI response generated from the context
    """
    try:
        json_wrapper = DataForSeoAPIWrapper(
            top_count=3,
            json_result_types=["organic", "local_pack"],
            json_result_fields=["title", "description", "type", "text"],
        )

        context = json_wrapper.results(user_prompt)

        response = chain.invoke(
            {"question": user_prompt, "context": context, "language": language, "traits": traits})

        return response, context
    except Exception as e:
        print(e)
        return "", {}
