import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("END_POINT")
)

deployment = os.getenv("DEPLOYMENT_NAME")

st.title("🏡 House Rent Prediction Agent")

query = st.text_area("Enter House details or rent prediction query.")

if st.button("Predict Rent"):

    response = client.chat.completions.create(
        model = deployment,
        messages = [
            {
                "role":"system",
                "content":"""
                        You are a house rent prediction agent. 
                        Analyze rental properties and provide rent estimates."""
            },
            {
                "role":"user",
                "content":query
            }
        ]
    )
    st.write(response.choices[0].message.content)