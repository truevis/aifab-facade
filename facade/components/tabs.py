import streamlit as st


def Tabs(tabs: list):
    """
    Themed tabs component.

    Args:
        tabs: List of tab label strings.

    Usage:
        tab1, tab2 = facade.Tabs(["Overview", "Settings"])
        with tab1:
            st.write("Overview")
        with tab2:
            st.write("Settings")
    """
    return st.tabs(tabs)