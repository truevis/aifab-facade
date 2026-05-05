import streamlit as st
from ..lucide import icon_html
from ..icons import to_lucide

_ICON_MAP = {
    "info":    "info",
    "success": "check",
    "warning": "warning",
    "error":   "error",
}

_VARIANT_TOKENS_LIGHT = {
    "info": {
        "bg":     "hsl(214, 80%, 92%)",   # more saturated blue
        "border": "hsl(214, 100%, 50%)",
        "text":   "hsl(214, 80%, 25%)",
    },
    "success": {
        "bg":     "hsl(142, 60%, 88%)",   # more saturated green
        "border": "hsl(142, 76%, 30%)",
        "text":   "hsl(142, 60%, 18%)",
    },
    "warning": {
        "bg":     "hsl(45, 90%, 88%)",    # more saturated yellow
        "border": "hsl(45, 100%, 40%)",
        "text":   "hsl(35, 80%, 22%)",
    },
    "error": {
        "bg":     "hsl(0, 75%, 92%)",     # more saturated red
        "border": "hsl(0, 86%, 45%)",
        "text":   "hsl(0, 70%, 25%)",
    },
}

_VARIANT_TOKENS_DARK = {
    "info": {
        "bg":     "hsl(214, 60%, 15%)",
        "border": "hsl(214, 100%, 60%)",
        "text":   "hsl(214, 80%, 80%)",
    },
    "success": {
        "bg":     "hsl(142, 40%, 12%)",
        "border": "hsl(142, 76%, 36%)",
        "text":   "hsl(142, 60%, 70%)",
    },
    "warning": {
        "bg":     "hsl(45, 60%, 12%)",
        "border": "hsl(45, 100%, 45%)",
        "text":   "hsl(45, 80%, 70%)",
    },
    "error": {
        "bg":     "hsl(0, 50%, 15%)",
        "border": "hsl(0, 86%, 50%)",
        "text":   "hsl(0, 70%, 75%)",
    },
}

_DARK_BACKGROUNDS = {
    "#0a0a08", "#0f172a", "#1e1e2e", "#1e293b",
    "#111827", "#09090b", "#000000", "#0a0f0e",
    "#050505", "#111110",
}


def Alert(
    message: str,
    title: str = None,
    variant: str = "info",
    icon: bool = True,
    key: str = None,
):
    """
    Themed alert box.

    Args:
        message:  Body text of the alert.
        title:    Optional bold heading above the message.
        variant:  "info" | "success" | "warning" | "error"
        icon:     Whether to show the leading icon.
        key:      Unused (reserved for API consistency).
    """
    bg_color = st.get_option("theme.backgroundColor") or "#ffffff"
    is_dark = bg_color.lower() in _DARK_BACKGROUNDS

    token_map = _VARIANT_TOKENS_DARK if is_dark else _VARIANT_TOKENS_LIGHT
    tokens = token_map.get(variant, token_map["info"])

    bg     = tokens["bg"]
    border = tokens["border"]
    color  = tokens["text"]

    icon_str = ""
    if icon:
        svg = icon_html(to_lucide(_ICON_MAP.get(variant, "info")), size=16, color=border)
        icon_str = f'<span style="display:flex;align-items:center;flex-shrink:0;margin-top:0.1rem;">{svg}</span>'

    title_html = (
        f'<p style="margin:0 0 0.2rem 0;font-weight:600;font-size:0.875rem;">{title}</p>'
    ) if title else ""

    html = (
        f'<div style="background:{bg};border-left:4px solid {border};border-radius:var(--radius,0.5rem);padding:0.75rem 1rem;display:flex;align-items:flex-start;gap:0.65rem;margin:0.5rem 0;">'
        f'{icon_str}'
        f'<div style="color:{color};font-size:0.875rem;line-height:1.5;">'
        f'{title_html}'
        f'<p style="margin:0;">{message}</p>'
        f'</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)