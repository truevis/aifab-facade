import streamlit as st


def TopBar(
    title: str = None,
    user: str = None,
    avatar: str = None,
):
    """
    Themed top bar for branding and context.
    Uses chrome tokens — same color as sidebar.

    Args:
        title:  App or current page title shown on the left.
        user:   Optional user name shown on the right.
        avatar: Optional single letter shown in avatar circle.

    Usage:
        facade.TopBar(
            title="My App",
            user="Daniyal",
            avatar="D",
        )
    """

    title_html = (
        f'<span style="'
        f'font-family:var(--font-sans);'
        f'font-size:0.9rem;'
        f'font-weight:600;'
        f'color:var(--chrome-foreground);'
        f'letter-spacing:0.01em;'
        f'">{title}</span>'
    ) if title else ""

    user_html = ""
    if user or avatar:
        avatar_html = ""
        if avatar:
            avatar_html = (
                f'<div style="'
                f'width:1.75rem;height:1.75rem;'
                f'border-radius:9999px;'
                f'background:var(--primary);'
                f'color:var(--primary-foreground);'
                f'display:flex;align-items:center;justify-content:center;'
                f'font-size:0.75rem;font-weight:600;'
                f'font-family:var(--font-sans);'
                f'flex-shrink:0;'
                f'">{avatar[0].upper()}</div>'
            )
        user_name_html = (
            f'<span style="'
            f'font-family:var(--font-sans);'
            f'font-size:0.875rem;'
            f'font-weight:500;'
            f'color:var(--chrome-foreground);'
            f'opacity:0.85;'
            f'">{user}</span>'
        ) if user else ""

        user_html = (
            f'<div style="display:flex;align-items:center;gap:0.5rem;">'
            f'{user_name_html}'
            f'{avatar_html}'
            f'</div>'
        )

    html = f"""
        <style>
            header[data-testid="stHeader"] {{
                background-color: var(--chrome-background) !important;
                border-bottom: 1px solid var(--chrome-border) !important;
                height: 3rem !important;
            }}
            div[data-testid="stToolbar"] {{
                background-color: var(--chrome-background) !important;
            }}
            .facade-topbar {{
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                height: 3rem;
                background: var(--chrome-background);
                border-bottom: 1px solid var(--chrome-border);
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 1.5rem;
                z-index: 998;
                box-sizing: border-box;
            }}
            .facade-topbar-left {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }}
            .facade-topbar-right {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }}
            .stMainBlockContainer {{
                padding-top: 4.5rem !important;
            }}
        </style>
        <div class="facade-topbar">
            <div class="facade-topbar-left">
                {title_html}
            </div>
            <div class="facade-topbar-right">
                {user_html}
            </div>
        </div>
    """

    st.markdown(html, unsafe_allow_html=True)