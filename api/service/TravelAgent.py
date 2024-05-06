from .init import agent_with_chat_history
from model.prompt import PromptResponse
import time
from dotenv import load_dotenv

load_dotenv(override=True)


def agent_chat(input:str, session_id:str)->str:

    start_time = time.time()

    results=agent_with_chat_history.invoke(
    {"input": input},
    config={"configurable": {"session_id": session_id}},
    )

    return  PromptResponse(text=results["output"],ResponseSeconds=(time.time() - start_time))