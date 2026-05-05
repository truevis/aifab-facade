import streamlit as st


def Checkbox(
    label: str,
    value: bool = False,
    disabled: bool = False,
    key: str = None,
) -> bool:
    """
    Themed checkbox component.

    Args:
        label:    Label text next to the checkbox.
        value:    Default checked state.
        disabled: Whether the checkbox is disabled.
        key:      Unique key for the widget.
    """
    return st.checkbox(
        label,
        value=value,
        disabled=disabled,
        key=key,
    )