import streamlit as st


def run():
    txt = st.text_area("paste text here")
    st.text("here is processed text")
    st.code(" ".join(txt.split("\n")[1::2]), language="plain")
