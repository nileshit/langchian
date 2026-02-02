import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama


load_dotenv()


def main():
    print("Hello from langchian!")

prompt = PromptTemplate(
    input_variables=["prodct","issue"],
    template="""
   You are a professional customer support agent.

The customer is contacting support regarding the following:

Product: {product}
Issue: {issue}

INSTRUCTIONS:
- Start your reply by mentioning the product name.
- Clearly acknowledge the customer's issue.
- Provide helpful troubleshooting guidance.
- Keep the tone polite and professional.
- Do NOT invent technical details.

Write the response now.
"""
)

formatted_prompt = prompt.format(
    product = "Air cooer",
    issue = "Not cooling properly"

)

chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.25
)
#ollama local llm
'''
chat_model = ChatOllama(
    model="gemma3:270m",
    temperature=0.25
)'''
chain = prompt | chat_model
response = chain.invoke({
    "product": "Air Cooler",
    "issue": "Not cooling properly"
})

print(response.content)

if __name__ == "__main__":
    main()
