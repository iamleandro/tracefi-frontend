import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("🔎 TraceFi")
st.subheader("Trace crypto wallets and follow the money")

if wallet := st.text_input("Enter wallet address:"):
    res = requests.get(f"{BACKEND_URL}/api/v1/health")
    st.write("Backend Health:", res.json())
