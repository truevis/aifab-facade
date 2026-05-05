import streamlit as st
from ..icons import to_material


def Button(
    label: str,
    variant: str = "default",
    size: str = "md",
    disabled: bool = False,
    icon: str = None,
    icon_position: str = "left",
    key: str = None,
) -> bool:
    """
    Themed button component.

    Args:
        label:         Button text.
        variant:       "default" | "outline" | "ghost" | "destructive"
        size:          "sm" | "md" | "lg"
        disabled:      Whether the button is disabled.
        icon:          facade icon name e.g. "save", "trash", "arrow-right"
        icon_position: "left" | "right"
        key:           Unique key for the widget.
    """
    uid = key or label.lower().replace(" ", "_")

    size_padding  = {"sm": "0.2rem 0.6rem", "md": "0.35rem 0.85rem",  "lg": "0.5rem 1.25rem"}
    font_size_map = {"sm": "0.8rem",           "md": "0.875rem",     "lg": "1rem"}

    padding   = size_padding.get(size,  size_padding["md"])
    font_size = font_size_map.get(size, font_size_map["md"])

    variant_css = {
        "default":     "background:var(--primary) !important;color:var(--primary-foreground) !important;border:2px solid transparent !important;",
        "outline":     "background:transparent !important;color:var(--primary) !important;border:2px solid var(--primary) !important;box-shadow:none !important;",
        "ghost":       "background:transparent !important;color:var(--foreground) !important;border:2px solid transparent !important;box-shadow:none !important;",
        "destructive": "background:var(--destructive) !important;color:#fff !important;border:2px solid transparent !important;",
    }
    hover_css = {
        "default":     "opacity:0.9 !important;",
        "outline":     "background:var(--primary) !important;color:var(--primary-foreground) !important;",
        "ghost":       "background:var(--muted) !important;",
        "destructive": "opacity:0.9 !important;",
    }

    style = variant_css.get(variant, variant_css["default"])
    hover = hover_css.get(variant, hover_css["default"])

    st.markdown(f"""
        <style>
            .st-key-{uid} button {{
                {style}
                padding: {padding} !important;
                font-size: {font_size} !important;
                border-radius: var(--radius) !important;
                font-family: var(--font-sans) !important;
                font-weight: 500 !important;
                width: auto !important;
                min-width: unset !important;
                transition: opacity 0.15s, background 0.15s !important;
            }}
            .st-key-{uid} button:hover {{ {hover} }}
        </style>
    """, unsafe_allow_html=True)

    material_icon = to_material(icon) if icon else None

    return st.button(
        label,
        key=uid,
        disabled=disabled,
        icon=material_icon,
        icon_position=icon_position,
    )