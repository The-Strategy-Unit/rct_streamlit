import os
import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

app_url = os.getenv("APP_URL")

st.title("Simple RCT uploader app")

file = st.file_uploader("Upload spreadsheet", type="csv")

email_subject = st.text_input("Email subject", width=250)

email_text = st.text_input(
    "Email text here please. The email will already begin 'Dear name_1 and name_2'"
)

if file and email_text:
    df = pd.read_csv(file)
    st.write(df)
    data_to_submit = df.to_json(orient="records")
    json_to_submit = {
        "key": os.getenv("API_KEY"),
        "data": data_to_submit,
        "email_subject": email_subject,
        "email_text": email_text,
    }
    if st.button("Submit emails"):
        response = requests.post(app_url, json=json_to_submit, timeout=120)
        st.write(response.text)
