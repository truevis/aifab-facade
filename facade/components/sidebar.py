import streamlit as st
import base64
import os


def _load_logo(logo: str) -> str:
    """Handles file path or URL. Returns img src string."""
    if logo.startswith("http://") or logo.startswith("https://"):
        return logo
    if not os.path.exists(logo):
        return None
    ext = os.path.splitext(logo)[1].lower()
    mime = "image/svg+xml" if ext == ".svg" else f"image/{ext.strip('.')}"
    with open(logo, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:{mime};base64,{b64}"


def Sidebar(
    logo: str = None,
    logo_width: int = 160,
    logo_height: int = None,
    title: str = None,
    footer: str = None,
    dividers: bool = False,
    active: str = None,
    nav_keys: dict = None,
):
    """
    Styled sidebar shell. Page switching logic handled by user.

    Args:
        logo:        File path or URL to logo image (svg, png, jpg)
        logo_width:  Logo width in px (default 160)
        logo_height: Logo height in px (default auto)
        title:       Sidebar title text shown below logo
        footer:      Footer text pinned to bottom of sidebar
        dividers:    Show divider lines after header and before footer
        active:      Currently active page name
        nav_keys:    Dict mapping page name to button key
    """
    if active and nav_keys and active in nav_keys:
        active_key = nav_keys[active]
        st.sidebar.markdown(f"""
            <style>
                [data-testid="stSidebar"] .st-key-{active_key} button {{
                    background: rgba(255,255,255,0.12) !important;
                    font-weight: 600 !important;
                }}
            </style>
        """, unsafe_allow_html=True)

    if footer:
        st.sidebar.markdown(f"""
            <style>
                .facade-sidebar-footer {{
                    position: fixed;
                    bottom: 1rem;
                    left: 0;
                    width: var(--sidebar-width, 18rem);
                    padding: 0 1.5rem;
                    font-size: 0.75rem;
                    color: var(--chrome-foreground);
                    opacity: 0.5;
                    font-family: var(--font-sans);
                    box-sizing: border-box;
                    pointer-events: none;
                    line-height: 1.4;
                }}
                .facade-sidebar-footer a {{
                    pointer-events: auto;
                    color: inherit;
                    text-decoration: underline;
                    text-underline-offset: 2px;
                }}
            </style>
        """, unsafe_allow_html=True)

    with st.sidebar:
        if logo:
            src = _load_logo(logo)
            if src:
                height_style = f"height:{logo_height}px;" if logo_height else "height:auto;"
                st.markdown(
                    f'<img src="{src}" style="width:{logo_width}px;{height_style}'
                    f'display:block;margin-bottom:2.0rem;">',
                    unsafe_allow_html=True,
                )
        if title:
            st.markdown(
                f'<div style="font-size:1rem;font-weight:600;'
                f'color:var(--chrome-foreground);margin-bottom:2.0rem;">'
                f'{title}</div>',
                unsafe_allow_html=True,
            )
        if dividers and (logo or title):
            st.markdown(
                '<hr style="border-color:var(--chrome-border);margin:0.5rem 0 0.75rem 0;">',
                unsafe_allow_html=True,
            )

    class _SidebarContext:
        def __enter__(self):
            self._ctx = st.sidebar.__enter__()
            return self._ctx

        def __exit__(self, *args):
            if dividers:
                st.sidebar.markdown(
                    '<hr style="border-color:var(--chrome-border);margin:0.75rem 0 0.5rem 0;">',
                    unsafe_allow_html=True,
                )
            if footer:
                st.sidebar.markdown(
                    f'<div class="facade-sidebar-footer">{footer}</div>',
                    unsafe_allow_html=True,
                )
            st.sidebar.__exit__(*args)

    return _SidebarContext()