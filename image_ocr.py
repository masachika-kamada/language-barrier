import streamlit as st
from PIL import Image
import pytesseract


def run():
    st.title("Image OCR")
    image = st.file_uploader("select image", type=["png","jpg"])
    if image:
        img = Image.open(image)
        st.image(img, width=350)
        txt = pytesseract.image_to_string(img, lang="eng")
        st.code(" ".join(txt.split("\n")), language="plain")
