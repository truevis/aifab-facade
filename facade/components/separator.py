import streamlit as st


def Separator(
    label: str = None,
    key: str = None,
):
    """
    Themed horizontal separator / divider.

    Args:
        label: Optional center label text.
        key:   Unused (reserved for API consistency).
    """
    if label:
        html = (
            f'<div style="'
            f'display:flex;align-items:center;gap:0.75rem;'
            f'margin:0.75rem 0;'
            f'">'
            f'<div style="flex:1;height:1px;background:var(--border);"></div>'
            f'<span style="'
            f'font-family:var(--font-sans);'
            f'font-size:0.75rem;'
            f'color:var(--muted-foreground);'
            f'white-space:nowrap;'
            f'">{label}</span>'
            f'<div style="flex:1;height:1px;background:var(--border);"></div>'
            f'</div>'
        )
    else:
        html = (
            f'<div style="'
            f'height:1px;'
            f'background:var(--border);'
            f'margin:0.75rem 0;'
            f'width:100%;'
            f'"></div>'
        )

    st.markdown(html, unsafe_allow_html=True)