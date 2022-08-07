import streamlit as st
from PIL import Image
import pytesseract


def run():
    st.title("OCR Programa")
    st.write("Optical Character Recognition (OCR) implementado com Python")
    imagem = st.file_uploader("Selecione alguma imagem", type=["png","jpg"])
    #se selecionar alguma imagem...
    if imagem:
        img = Image.open(imagem)
        st.image(img, width=350)
        st.info("Texto extraído")
        texto = extrair_texto(img)
        st.write("{}".format(texto))

        analisar_texto = st.sidebar.checkbox("Analisar texto")


def extrair_texto(img):
    texto = pytesseract.image_to_string(img, lang="eng")
    return texto
