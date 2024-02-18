import os
import google.generativeai as genai
from constants import gemini_key
import streamlit as st

st.image("https://t3.ftcdn.net/jpg/05/67/13/22/360_F_567132273_mfAcrOWFm37aF7gbKtgqOQCEQpUQBo9v.jpg", width = 200, caption = "Gemini-pro AI Model")
st.title("Article Summarization using Gemini-pro AI Model")
st.write("This app uses the Gemini-pro AI model to summarize articles and provide recent article links based on the topic name you provide.")
os.environ['GOOGLE_API_KEY'] = gemini_key
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')


user_input = st.text_area("Enter Topic name of article you're looking for:")
button = st.button('Search Articles')
if user_input and button:
    response = model.generate_content('Give recent article links and a brief summary of articles based on this : ' + user_input)
    st.balloons()
    st.write(response.text)

user_input = st.text_area("Enter the article link you want to summarize:")
urlbutton = st.button('Summarize')
if user_input and urlbutton:
    response = model.generate_content('Give summary of article in 100 words, find relevant keywords and highlight them, and at last suggest articles related to this one, given in the link: ' + user_input)
    st.write(response.text)