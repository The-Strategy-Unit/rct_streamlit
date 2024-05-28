import os
import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

app_url = os.getenv("APP_URL")

st.title("Simple RCT uploader app")

file = st.file_uploader("Upload spreadsheet", type="csv")

if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    json_to_submit = df.to_json(orient="records")
    if st.button("Submit emails"):
        response = requests.post(app_url, json=json_to_submit, timeout=120)
        st.write(response.text)
