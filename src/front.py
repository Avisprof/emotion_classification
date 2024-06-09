import streamlit as st
import requests

st.title("Emoton classification")
text = st.text_input("Enter text")

result = st.button("Predict emotion")
if result:
    resp = requests.post(url="http://127.0.0.1:8000/predict/", data={"text": text})
    st.write("**Result**")
    st.write(resp.json())