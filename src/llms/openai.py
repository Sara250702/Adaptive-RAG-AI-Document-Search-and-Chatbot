"""
Mistral LLM initialization and configuration.
"""

import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY", "")

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)