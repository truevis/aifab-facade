import streamlit as st
from typing import List


def Select(options: List[str], placeholder: str = "Select...", label: str = None, key: str = None) -> str:
    choices = [placeholder] + options
    result = st.selectbox(
        label or placeholder,
        choices,
        key=key,
        label_visibility= "visible" if label else "collapsed"
    )
    return result if result != placeholder else None