import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable, RunnableConfig
from typing import cast
from helpers.tools import find_info_on_fhswf_website
from langchain.agents import create_tool_calling_agent, AgentExecutor
from helpers.prompts import prompt


@cl.on_chat_start
async def on_chat_start():
    model = ChatOpenAI(model="gpt-4o", streaming=True)
    tools = [find_info_on_fhswf_website]
    agent = create_tool_calling_agent(model, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)
    cl.user_session.set("agent_executor", agent_executor)


@cl.on_message
async def main(message: cl.Message):
    agent_executor = cast(AgentExecutor, cl.user_session.get("agent_executor"))
    msg = cl.Message(content="")
    #async for chunk in agent_executor.astream(
    #    {"question": message.content},
        # config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    #):
    #    await msg.stream_token(chunk)
    result = await agent_executor.ainvoke({"question": message.content})
    print(result)
    msg.content = result["output"]
    await msg.send()