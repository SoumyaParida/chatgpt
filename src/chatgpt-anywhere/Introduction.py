import streamlit as st
import os
import openai


app_title = os.environ.get("APP_TITLE", "ChatGPT Anywhere in Streamlit App")
st.title(app_title)