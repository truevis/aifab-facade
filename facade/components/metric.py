import streamlit as st


def Metric(
    label: str,
    value,
    delta=None,
    delta_color: str = "normal",
    key: str = None,
):
    """
    Themed metric component for KPIs and stats.

    Args:
        label:       Metric label.
        value:       Main value to display (str, int, float).
        delta:       Optional change indicator e.g. "12%" or "-5".
        delta_color: "normal" | "inverse" | "off"
        key:         Unused (reserved for API consistency).
    """
    # Determine delta color for display
    delta_html = ""
    if delta is not None:
        val = str(delta)
        is_negative = val.startswith("-")
        if delta_color == "off":
            color = "var(--muted-foreground)"
            arrow = ""
        elif delta_color == "inverse":
            color = "hsl(142, 76%, 36%)" if is_negative else "hsl(0, 86%, 50%)"
            arrow = "↓ " if is_negative else "↑ "
        else:
            color = "hsl(0, 86%, 50%)" if is_negative else "hsl(142, 76%, 36%)"
            arrow = "↓ " if is_negative else "↑ "

        delta_html = (
            f'<div style="margin-top:0.4rem;font-size:1rem;font-weight:500;color:{color};">'
            f'{arrow}{val}'
            f'</div>'
        )

    html = (
        f'<div style="'
        f'background:var(--muted);'
        f'border:1px solid var(--border);'
        f'border-radius:var(--radius);'
        f'padding:1rem 1.25rem;'
        f'width:100%;'
        f'box-sizing:border-box;'
        f'">'
        f'<div style="font-family:var(--font-sans);font-size:0.875rem;font-weight:500;color:var(--muted-foreground);">{label}</div>'
        f'<div style="font-family:var(--font-sans);font-size:2rem;font-weight:600;color:var(--foreground);line-height:1.2;margin-top:0.25rem;">{value}</div>'
        f'{delta_html}'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)