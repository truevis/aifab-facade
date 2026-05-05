import streamlit as st
from ..lucide import icon_html
from ..icons import to_lucide


def IconCard(
    title: str = None,
    description: str = None,
    icon: str = None,
    icon_size: int = 24,
    key: str = None,
):
    """
    Themed card component with an optional leading icon.

    Args:
        title:       Card heading text.
        description: Supporting text below the title.
        icon:        facade icon name e.g. "zap", "code", "settings"
        icon_size:   Icon size in pixels (default 24).
        key:         Unused (reserved for API consistency).

    Usage:
        facade.IconCard(
            title="No build pipeline",
            description="Pure Python. No Node, no npm, no React.",
            icon="zap",
        )
    """
    icon_html_str = ""
    if icon:
        lucide_name = to_lucide(icon)
        svg = icon_html(lucide_name, size=icon_size, color="var(--primary)")
        icon_html_str = f'<div style="margin-bottom:0.75rem;">{svg}</div>'

    title_html = (
        f'<div style="font-size:1rem;font-weight:600;color:var(--foreground);margin-bottom:0.25rem;">{title}</div>'
    ) if title else ""

    description_html = (
        f'<div style="font-size:0.875rem;color:var(--muted-foreground);">{description}</div>'
    ) if description else ""

    st.markdown(f"""
        <div style="
            background: var(--muted);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.25rem 1.5rem;
            font-family: var(--font-sans);
            margin-bottom: 1rem;
        ">
            {icon_html_str}
            {title_html}
            {description_html}
        </div>
    """, unsafe_allow_html=True)