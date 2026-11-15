import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set. Add it to your .env file.")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
)

prompt = """Give me exactly 5 healthy breakfast ideas.

Requirements:
- Number them 1 through 5.
- Write exactly one breakfast idea per line.
- Do not include a preamble or conclusion.
- Each breakfast should include a high-fiber carbohydrate, a protein source, and fruit or vegetables.
- Avoid heavily processed foods and excessive added sugar.
"""

reply = llm.invoke(prompt)
print(reply.content)
