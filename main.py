import os
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

tavily = TavilyClient()
@tool
def search(query: str) -> str:
    '''
    Search the web for real-time information based on a query.

    Args:
        query (str): The specific search term or question to look up.

    Returns:
        str: A summary of search results or the raw text from the top result.
   '''
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash",
    temperature=0.25)
tools = [search]
agent = create_agent(model=llm,tools=tools)


def main():
    print("Hello from langchian!")
    result = agent.invoke({"messages":HumanMessage(content="three job postings for an AI engineer in Langchain in the Maharastra area in LinkedIn")})
    print(result)
if __name__ == "__main__":
    main()
