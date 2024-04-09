from dotenv import load_dotenv
from langchain.globals import set_llm_cache
from langchain_openai import ChatOpenAI



load_dotenv(override=True)


chat : ChatOpenAI | None=None
chat_history:list

def LLM_init():
    global chat,chat_history
    chat = ChatOpenAI(model_name="gpt-3.5-turbo-16k",temperature=0)
    chat_history = []

LLM_init()