"""
ReAct agent setup for document retrieval and question answering.
"""

import os

from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

from src.config.settings import Config
from src.llms.openai import llm
from src.rag.retriever_setup import get_retriever

config = Config()

# Initialize tools
# Initialize tools
@tool("retriever_customer_uploaded_documents")
def retrieve_uploaded_documents(query: str) -> str:
    """Search the currently uploaded document for information relevant to a question."""
    return get_retriever().invoke(query)


tools = [retrieve_uploaded_documents]

# Load document description if available
if os.path.exists("description.txt"):
    with open("description.txt", "r", encoding="utf-8") as f:
        description = f.read()
else:
    description = None

# Create ReAct agent prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", config.prompt("system_prompt")),
    ("human", "{input}\n\n{agent_scratchpad}")
])

# Initialize the ReAct agent and executor
react_agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=react_agent,
    tools=tools,
    handle_parsing_errors=True,
    max_iterations=2,
    verbose=False,
    return_intermediate_steps=True
)
