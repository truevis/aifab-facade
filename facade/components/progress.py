import streamlit as st


def Progress(
    value: int,
    label: str = None,
    key: str = None,
):
    """
    Themed progress bar component.

    Args:
        value: Progress value between 0 and 100.
        label: Optional label text above the bar.
        key:   Unused (reserved for API consistency).
    """
    value = max(0, min(100, value))

    pct = value / 100
    bar_color = "var(--primary)"
    track_color = "var(--muted)"

    label_html = (
        f'<div style="font-family:var(--font-sans);font-size:0.875rem;font-weight:500;color:var(--foreground);margin-bottom:0.35rem;">{label}</div>'
    ) if label else ""

    html = (
        f'<div style="margin:0.25rem 0 0.75rem 0;">'
        f'{label_html}'
        f'<div style="background:{track_color};border-radius:9999px;height:0.5rem;width:100%;">'
        f'<div style="background:{bar_color};border-radius:9999px;height:100%;width:{pct*100}%;transition:width 0.3s ease;"></div>'
        f'</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)