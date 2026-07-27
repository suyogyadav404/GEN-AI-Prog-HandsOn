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

st.title("GPT-5 Chat App")

question = st.text_input("Ask Anything")

if st.button("Send"):
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role":"user","content":question}
        ]
    )

    st.write(response.choices[0].message.content)