import streamlit as st
import os
import openai


app_title = os.environ.get("APP_TITLE", "ChatGPT Anywhere")
st.title(app_title)