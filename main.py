from prompt import prompt
from llm import llm
from parser import ReviewAnalysis

structured_llm = llm.with_structured_output(ReviewAnalysis)

chain = prompt | structured_llm

review = "The phone looks good but battery drains quickly."

response = chain.invoke({
    "review": review
})

print(response)