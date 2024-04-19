from .init import chat, chat_history
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
from service import TravelAgentTools as agent_tools
from model.promptresponse import PromptResponse
import time
from os import environ
from dotenv import load_dotenv

load_dotenv(override=True)


def agent_chat(input:str, session_id:str)->str:

    
    tools = [agent_tools.vacation_lookup, agent_tools.itinerary_lookup, agent_tools.book_cruise ]
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful and friendly travel assistant for a cruise company. Answer travel questions to the best of your ability providing only relevant information. In order to book a cruise you will need to capture the person's name.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "Answer should be embedded in html tags. {input}"),
         MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
    )

    #Answer should be embedded in html tags. Only answer questions related to cruise travel, If you can not answer respond with \"I am here to assist with your travel questions.\". 

    llm_with_tools = chat.bind_tools(tools)

    #agent = (
    #{
    #    "input": lambda x: x["input"],
    #    "agent_scratchpad": lambda x: format_to_openai_tool_messages(
    #        x["intermediate_steps"]
    #    ),
       #  "chat_history": lambda x: x["chat_history"]
    #}
    #| prompt
    #| llm_with_tools
    #| OpenAIToolsAgentOutputParser()
    #)

 

    agent = create_openai_tools_agent(chat, tools, prompt)
    agent_executor  = AgentExecutor(agent=agent, tools=tools, verbose=True)

    agent_with_chat_history = RunnableWithMessageHistory(
        agent_executor,
        # This is needed because in most real world scenarios, a session id is needed
        # It isn't really used here because we are using a simple in memory ChatMessageHistory
        lambda sessionid: MongoDBChatMessageHistory( database_name="travel",
                                                 collection_name="history",
                                                   connection_string=environ.get("MONGO_CONNECTION_STRING"),
                                                   session_id=sessionid),
        input_messages_key="input",
        history_messages_key="chat_history",
)

    start_time = time.time()
    #results = agent_executor.invoke({"input": input,"chat_history": chat_history})
    results=agent_with_chat_history.invoke(
    {"input": input},
    config={"configurable": {"session_id": session_id}},
)
    #chat_history.extend(
    #[
    #    HumanMessage(content=input),
    #    AIMessage(content=results["output"])
    #]
   # )
    return  PromptResponse(text=results["output"],ResponseSeconds=(time.time() - start_time))