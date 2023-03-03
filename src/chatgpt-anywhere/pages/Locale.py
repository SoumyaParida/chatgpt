import streamlit as st


st.title("Choose Locale")


en_locale = st.button(label='EN', key='en')
ru_locale = st.button(label='RU', key='ru')

if en_locale and not ru_locale:
	st.session_state["Locale"] = "en"
else:
	st.session_state["Locale"] = "ru"