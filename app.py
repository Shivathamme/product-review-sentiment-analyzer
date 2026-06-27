import streamlit as st

from prompt import prompt
from llm import llm
from parser import ReviewAnalysis

# Structured Output
structured_llm = llm.with_structured_output(ReviewAnalysis)

chain = prompt | structured_llm

st.set_page_config(
    page_title="Product Review Sentiment Analyzer",
    page_icon="⭐"
)

st.title("⭐ Product Review Sentiment Analyzer")

review = st.text_area(
    "Enter Product Review",
    height=150
)

if st.button("Analyze Review"):

    if review.strip():

        response = chain.invoke({
            "review": review
        })

        st.subheader("Analysis Result")

        st.json({
            "sentiment": response.sentiment,
            "sentiment_score": response.sentiment_score,
            "key_points": response.key_points,
            "summary": response.summary
        })

    else:
        st.warning("Please enter a review.")