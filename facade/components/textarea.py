import streamlit as st


def Textarea(
    placeholder: str = "",
    label: str = None,
    height: int = 120,
    max_chars: int = None,
    key: str = None,
) -> str:
    """
    Themed textarea component.

    Args:
        placeholder: Placeholder text.
        label:       Optional label above the textarea.
        height:      Height in pixels (default 120).
        max_chars:   Optional character limit.
        key:         Unique key for the widget.
    """
    return st.text_area(
        label or placeholder,
        placeholder=placeholder,
        height=height,
        max_chars=max_chars,
        key=key,
        label_visibility="collapsed" if not label else "visible",
    )