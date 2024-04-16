from .init import chat, chat_history
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from service import TravelAgentTools as agent_tools
from model.promptresponse import PromptResponse
import time





def agent_chat(input:str)->str:

    tools = [agent_tools.vacation_lookup, agent_tools.itinerary_lookup, agent_tools.book_cruise ]
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful and friendly travel assistant for a cruise company. Answer all questions to the best of your ability providing only relevant information. In order to book a cruise you will need to capture the person's name.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "Answer should be embedded in html tags. {input}"),
         MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
    )

    #Answer should be embedded in html tags. 

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

    start_time = time.time()
    results = agent_executor.invoke({"input": input,"chat_history": chat_history})

    chat_history.extend(
    [
        HumanMessage(content=input),
        AIMessage(content=results["output"])
    ]
    )
    return  PromptResponse(text=results["output"],ResponseSeconds=(time.time() - start_time))