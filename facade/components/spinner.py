import streamlit as st
from contextlib import contextmanager


@contextmanager
def Spinner(label: str = "Loading..."):
    """
    Themed spinner / loading indicator.

    Args:
        label: Text shown next to the spinner.

    Usage:
        with facade.Spinner("Loading data..."):
            time.sleep(2)
    """
    with st.spinner(label):
        yield