import streamlit as st


_VARIANT_TOKENS = {
    "default": {
        "bg":     "var(--primary)",
        "text":   "var(--primary-foreground)",
        "border": "var(--primary)",
    },
    "success": {
        "bg":     "hsl(142, 76%, 95%)",
        "text":   "hsl(142, 60%, 20%)",
        "border": "hsl(142, 76%, 36%)",
    },
    "warning": {
        "bg":     "hsl(45, 100%, 95%)",
        "text":   "hsl(35, 80%, 25%)",
        "border": "hsl(45, 100%, 45%)",
    },
    "error": {
        "bg":     "hsl(0, 86%, 97%)",
        "text":   "hsl(0, 70%, 30%)",
        "border": "hsl(0, 86%, 50%)",
    },
    "outline": {
        "bg":     "transparent",
        "text":   "var(--foreground)",
        "border": "var(--border)",
    },
    "muted": {
        "bg":     "var(--muted)",
        "text":   "var(--muted-foreground)",
        "border": "var(--muted)",
    },
}


def Badge(
    text: str,
    variant: str = "default",
    bg_color: str = None,
    text_color: str = None,
    border_color: str = None,
    key: str = None,
):
    """
    Themed badge / pill component.

    Args:
        text:         Text inside the badge.
        variant:      "default" | "success" | "warning" | "error" | "outline" | "muted"
        bg_color:     Optional custom background color, overrides variant.
        text_color:   Optional custom text color, overrides variant.
        border_color: Optional custom border color, defaults to bg_color if not set.
        key:          Unused (reserved for API consistency).
    """
    tokens = _VARIANT_TOKENS.get(variant, _VARIANT_TOKENS["default"])

    bg     = bg_color     or tokens["bg"]
    text_c = text_color   or tokens["text"]
    border = border_color or bg_color or tokens["border"]

    html = (
        f'<span style="'
        f'display:inline-flex;align-items:center;'
        f'background:{bg};'
        f'color:{text_c};'
        f'border:1px solid {border};'
        f'border-radius:9999px;'
        f'padding:0.15rem 0.65rem;'
        f'font-size:0.75rem;'
        f'font-weight:500;'
        f'font-family:var(--font-sans);'
        f'line-height:1.5;'
        f'white-space:nowrap;'
        f'">{text}</span>'
    )
    st.markdown(html, unsafe_allow_html=True)