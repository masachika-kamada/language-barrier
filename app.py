import streamlit as st
import reshape_sentence
import image_ocr


def sidebar():
    with st.sidebar:
        func_select = st.radio(
            "機能切替",
            ("文字整形",
             "OCR")
        )

    return func_select


def main():
    func = sidebar()

    if func == "文字整形":
        reshape_sentence.run()
    elif func == "OCR":
        image_ocr.run()


if __name__ == '__main__':
    main()
