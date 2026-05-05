import streamlit as st


def Toggle(
    label: str,
    value: bool = False,
    disabled: bool = False,
    key: str = None,
):
    """
    Themed toggle/switch component.

    Args:
        label:    Label next to the toggle.
        value:    Default state.
        disabled: Whether the toggle is disabled.
        key:      Unique key for the widget.
    """
    return st.toggle(
        label,
        value=value,
        disabled=disabled,
        key=key,
    )