import streamlit as st
import requests

st.title("Emotion classification")
text = st.text_input("Enter text")

result = st.button("Predict emotion")
if result:
    resp = requests.post(url="http://fastapi_app:8000/api/predict/", json={"text": text})
    st.write("**Result**")
    st.write(resp.json())

hc = st.button("Healthcheck")
if hc:
    resp = requests.get("http://fastapi_app:8000/api/healthcheck")
    st.write(f"Healthchek: {resp.json()}")