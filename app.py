import streamlit as st
import pickle

# Load trained model
with open("fake_news_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("📰 Fake News Detection App")
st.write("Enter a news article below to check whether it is **Fake** or **Real**.")

# Text input
news_text = st.text_area("Enter News Text", height=200)

# Predict button
if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some text")
    else:
        prediction = model.predict([news_text])[0]

        if prediction == 1:
            st.success("✅ This news is **REAL**")
        else:
            st.error("🚨 This news is **FAKE**")
