import streamlit as st
from contextlib import contextmanager

@contextmanager
def StyledContainer(
    border: str = "all",
    border_color: str = "var(--border)",
    border_width: str = "2px",
    border_surround_color: str = "var(--border)",  # color for the other 3 sides when border != "all"
    background: str = "var(--muted)",
    radius: str = "var(--radius)",
    padding: str = "1.25rem 1.5rem",
    key: str = None,
):
    if key is None:
        raise ValueError("StyledContainer requires a unique `key`.")

    border_prop = {
        "top":    "border-top",
        "bottom": "border-bottom",
        "left":   "border-left",
        "right":  "border-right",
        "all":    "border",
        "none":   "",
    }.get(border, "border")

    accent_rule = (
        border_prop + ": " + border_width + " solid " + border_color + ";"
        if border_prop else ""
    )

    # build surround rules for the other 3 sides
    surround_rule = ""
    if border == "top":
        surround_rule = (
            "border-left: 1px solid " + border_surround_color + ";"
            "border-right: 1px solid " + border_surround_color + ";"
            "border-bottom: 1px solid " + border_surround_color + ";"
        )
    elif border == "bottom":
        surround_rule = (
            "border-left: 1px solid " + border_surround_color + ";"
            "border-right: 1px solid " + border_surround_color + ";"
            "border-top: 1px solid " + border_surround_color + ";"
        )
    elif border == "left":
        surround_rule = (
            "border-top: 1px solid " + border_surround_color + ";"
            "border-right: 1px solid " + border_surround_color + ";"
            "border-bottom: 1px solid " + border_surround_color + ";"
        )
    elif border == "right":
        surround_rule = (
            "border-top: 1px solid " + border_surround_color + ";"
            "border-left: 1px solid " + border_surround_color + ";"
            "border-bottom: 1px solid " + border_surround_color + ";"
        )

    css = (
        "<style>"
        ".st-key-" + key + " {"
        "  background: " + background + " !important;"
        "  " + accent_rule +
        "  " + surround_rule +
        "  border-radius: " + radius + ";"
        "  padding: " + padding + ";"
        "  margin-bottom: 1rem;"
        "}"
        "</style>"
    )

    st.markdown(css, unsafe_allow_html=True)

    with st.container(key=key):
        yield