import streamlit as st


def Radio(
    options: list,
    label: str = "",
    index: int = 0,
    horizontal: bool = False,
    disabled: bool = False,
    key: str = None,
) -> str:
    """
    Themed radio button group.

    Args:
        options:    List of option strings.
        label:      Label above the radio group.
        index:      Default selected index.
        horizontal: Whether to render options inline.
        disabled:   Whether the radio group is disabled.
        key:        Unique key for the widget.
    """
    return st.radio(
        label or "",
        options=options,
        index=index,
        horizontal=horizontal,
        disabled=disabled,
        key=key,
        label_visibility="collapsed" if not label else "visible",
    )