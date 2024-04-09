from .init import chat, chat_history
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_core.messages import AIMessage, HumanMessage

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import json

from service import TravelAgentTools as agent_tools







def agent_chat(input:str)->str:

    tools = [agent_tools.travel_search ]
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful travel assistant for a cruise company. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
         MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
    )


    llm_with_tools = chat.bind_tools(tools)

    agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
         "chat_history": lambda x: x["chat_history"]
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
    )


    agent_executor  = AgentExecutor(agent=agent, tools=tools, verbose=True)
    results = agent_executor.invoke({"input": input,"chat_history": chat_history})

    chat_history.extend(
    [
        HumanMessage(content=input),
        AIMessage(content=results["output"])
    ]
    )
    return results["output"]