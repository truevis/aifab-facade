import streamlit as st


def Input(placeholder: str = "", label: str = None, key: str = None) -> str:
    return st.text_input(
        label or placeholder,
        placeholder=placeholder,
        key=key,
        label_visibility="collapsed" if not label else "visible"
    )