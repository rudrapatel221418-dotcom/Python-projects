import streamlit as st
from textblob import TextBlob


st.title("Emotion Detector App")
st.write("Enter some text below to analyze its emotional tone.")

user_text = st.text_area("Enter Text:", placeholder="Type here...")


if st.button("Analyze Emotion"):
    if user_text.strip() != "":
        
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity

        
        if polarity > 0.5:
            category = "Very Positive"
            color = "green"
        elif 0 < polarity <= 0.5:
            category = "Slightly Positive"
            color = "lightgreen"
        elif polarity == 0:
            category = "Neutral"
            color = "gray"
        else:
            category = "Negative"
            color = "red"
        
        
        st.divider()
        st.subheader("Results")
        st.write(f"**Polarity Score:** {polarity:.2f}")
        st.markdown(f"**Emotion Category:** :{color}[{category}]")
    else:
        st.warning("Please enter some text before analyzing.")
        