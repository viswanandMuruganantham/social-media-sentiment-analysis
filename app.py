# app.py

import streamlit as st
from sentiment_analysis import analyze_sentiment

st.set_page_config(page_title="Social Media Sentiment Analyzer")
st.title("🧠 Social Media Sentiment Analyzer")
st.markdown("Analyze the sentiment of any social media post! 💬")

user_input = st.text_area("Enter your post/tweet here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        result = analyze_sentiment(user_input)
        st.success(f"Predicted Sentiment: **{result}**")
