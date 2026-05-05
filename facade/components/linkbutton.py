import streamlit as st
from ..icons import to_material


def LinkButton(
    label: str,
    url: str,
    variant: str = "default",
    size: str = "md",
    disabled: bool = False,
    icon: str = None,
    icon_position: str = "left",
    key: str = None,
) -> None:
    """
    Themed link button component. Navigates to a URL on click.
    Visually identical to facade.Button — same variants, sizes, and icons.

    Args:
        label:         Button text.
        url:           URL to navigate to when clicked.
        variant:       "default" | "outline" | "ghost" | "destructive"
        size:          "sm" | "md" | "lg"
        disabled:      Whether the button is disabled.
        icon:          facade icon name e.g. "external-link", "github", "arrow-right"
        icon_position: "left" | "right"
        key:           Unique key for the widget.

    Usage:
        facade.LinkButton("GitHub", url="https://github.com/itsdaniyalm/streamlit-facade", variant="outline", icon="external-link")
        facade.LinkButton("Docs", url="https://docs.example.com", variant="default", icon="file")
        facade.LinkButton("PyPI", url="https://pypi.org/project/streamlit-facade", variant="ghost", size="sm")
    """
    uid = key or label.lower().replace(" ", "_")

    size_padding  = {"sm": "0.25rem 0.75rem", "md": "0.5rem 1rem",  "lg": "0.75rem 1.5rem"}
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
            .st-key-{uid} a {{
                {style}
                padding: {padding} !important;
                font-size: {font_size} !important;
                border-radius: var(--radius) !important;
                font-family: var(--font-sans) !important;
                font-weight: 500 !important;
                width: auto !important;
                min-width: 6rem !important;
                transition: opacity 0.15s, background 0.15s !important;
                text-decoration: none !important;
            }}
            .st-key-{uid} a:hover {{ {hover} }}
        </style>
    """, unsafe_allow_html=True)

    material_icon = to_material(icon) if icon else None

    st.link_button(
        label,
        url=url,
        key=uid,
        disabled=disabled,
        icon=material_icon,
        icon_position=icon_position,
    )