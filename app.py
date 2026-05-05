"""
Interactive playground for streamlit-facade — exercises themes, layout, form,
display, icons, and utilities from https://github.com/itsdaniyalm/streamlit-facade
"""

from __future__ import annotations

import importlib
import datetime
import time
from pathlib import Path

import pandas as pd
import streamlit as st

import facade

_facade_theme_mod = importlib.import_module("facade.theme")
# Hays Electrical Services (https://www.hayselectrical.com/) — Wix :root RGB tokens sampled from the live homepage.
_facade_theme_mod._PRESETS["electric"] = {
    "primary": "#F42814",
    "primary_foreground": "#FFFFFF",
    "background": "#FFFFFF",
    "foreground": "#000000",
    "muted": "#E8E6E6",
    "muted_foreground": "#757575",
    "border": "#C7C7C7",
    "destructive": "#D1000A",
    "chrome_background": "#000000",
    "chrome_foreground": "#FFFFFF",
    "chrome_border": "#2E2E2E",
    "font_sans": "Montserrat, system-ui, sans-serif",
    "font_mono": "monospace",
    "radius": "0.5rem",
}


def _facade_link_button_compat(
    label: str,
    url: str,
    *,
    variant: str = "default",
    size: str = "md",
    disabled: bool = False,
    icon: str | None = None,
    icon_position: str = "left",
    css_key: str,
) -> None:
    """
    Same styling as facade.LinkButton, but does not pass ``key`` to
    ``st.link_button`` (Streamlit < ~1.56 omits ``key`` on link buttons).
    Uses ``st.container(key=css_key)`` so themed CSS still scopes correctly.
    """
    uid = css_key
    size_padding = {"sm": "0.25rem 0.75rem", "md": "0.5rem 1rem", "lg": "0.75rem 1.5rem"}
    font_size_map = {"sm": "0.8rem", "md": "0.875rem", "lg": "1rem"}
    padding = size_padding.get(size, size_padding["md"])
    font_size = font_size_map.get(size, font_size_map["md"])
    variant_css = {
        "default": (
            "background:var(--primary) !important;color:var(--primary-foreground) "
            "!important;border:2px solid transparent !important;"
        ),
        "outline": (
            "background:transparent !important;color:var(--primary) !important;"
            "border:2px solid var(--primary) !important;box-shadow:none !important;"
        ),
        "ghost": (
            "background:transparent !important;color:var(--foreground) !important;"
            "border:2px solid transparent !important;box-shadow:none !important;"
        ),
        "destructive": (
            "background:var(--destructive) !important;color:#fff !important;"
            "border:2px solid transparent !important;"
        ),
    }
    hover_css = {
        "default": "opacity:0.9 !important;",
        "outline": (
            "background:var(--primary) !important;"
            "color:var(--primary-foreground) !important;"
        ),
        "ghost": "background:var(--muted) !important;",
        "destructive": "opacity:0.9 !important;",
    }
    style = variant_css.get(variant, variant_css["default"])
    hover = hover_css.get(variant, hover_css["default"])
    material_icon = facade.to_material(icon) if icon else None

    with st.container(key=uid):
        st.markdown(
            f"""
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
            """,
            unsafe_allow_html=True,
        )
        st.link_button(
            label,
            url,
            disabled=disabled,
            icon=material_icon,
            icon_position=icon_position,
        )


PRESETS = [
    "default",
    "default-dark",
    "carbon-sage",
    "carbon-sage-dark",
    "carbon-light",
    "carbon-dark",
    "carbon-amber",
    "burgundy",
    "electric",
    "minimal",
    "warm",
    "dark",
    "daniyal",
]

# streamlit-facade applies preset colors via CSS; ``base`` alone only updates
# ``.streamlit/config.toml`` for Streamlit chrome. Map light↔dark preset pairs
# so the Base radio actually swaps façade tokens where pairs exist.
_PRESET_LIGHT_TO_DARK: dict[str, str] = {
    "default": "default-dark",
    "carbon-sage": "carbon-sage-dark",
    "carbon-light": "carbon-dark",
}
_PRESET_DARK_TO_LIGHT: dict[str, str] = {v: k for k, v in _PRESET_LIGHT_TO_DARK.items()}


def _effective_preset_for_base(preset: str, base: str) -> str:
    """Return the façade preset whose token palette matches ``base`` when a pair exists."""
    if base == "dark":
        if preset in _PRESET_LIGHT_TO_DARK:
            return _PRESET_LIGHT_TO_DARK[preset]
        return preset
    # light
    if preset in _PRESET_DARK_TO_LIGHT:
        return _PRESET_DARK_TO_LIGHT[preset]
    if preset == "dark":
        return "default"
    return preset


_app_dir = Path(__file__).resolve().parent
_favicon = _app_dir / "img" / "favicon.ico"

st.set_page_config(
    page_title="streamlit-facade playground",
    page_icon=str(_favicon),
    layout="wide",
    initial_sidebar_state="expanded",
)

defaults = {
    "demo_preset": "carbon-sage",
    "demo_base": "light",
    "demo_radius": "md",
    "demo_primary": "",
    "demo_icon_filter": "home",
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

_UPSTREAM_REPO = "https://github.com/itsdaniyalm/streamlit-facade"
with facade.Sidebar(
    title="Playground",
    footer=(
        "Shadcn-inspired UI components for Streamlit. "
        f"This app vendors the <code>facade</code> package (v{facade.__version__}). "
        f'Upstream: <a href="{_UPSTREAM_REPO}" target="_blank" rel="noopener noreferrer">'
        "streamlit-facade on GitHub</a>."
    ),
    dividers=True,
):
    st.markdown("**Theme**")
    st.selectbox("Preset", PRESETS, key="demo_preset")
    st.radio("Base", ["light", "dark"], horizontal=True, key="demo_base")
    # Streamlit uses `stMarkdownContainer`, not `stMarkdown`; façade only styles the
    # latter, so plain `st.markdown` / `st.caption` keep Streamlit light-theme body
    # color on dark chrome. Inline chrome token on real HTML avoids that mismatch.
    st.html(
        "<p style=\"margin:0;padding:0;font-size:0.8125rem;line-height:1.35;"
        "color:var(--chrome-foreground);font-family:var(--font-sans);\">"
        "Uses the preset's dark variant when available (default, carbon-sage, "
        "carbon-light pairs). Others follow the preset's own palette."
        "</p>"
    )
    st.selectbox(
        "Radius",
        ["xxs", "sm", "md", "lg", "xl"],
        key="demo_radius",
    )
    st.text_input(
        "Primary override (hex, optional)",
        key="demo_primary",
        placeholder="#1059A0",
    )

_effective_preset = _effective_preset_for_base(
    st.session_state.demo_preset,
    st.session_state.demo_base,
)
apply_kw = {
    "preset": _effective_preset,
    "base": st.session_state.demo_base,
    "radius": st.session_state.demo_radius,
}
if _effective_preset == "electric":
    apply_kw["font_sans"] = _facade_theme_mod._PRESETS["electric"]["font_sans"]
    apply_kw["font_link"] = (
        "https://fonts.googleapis.com/css2?"
        "family=Montserrat:wght@400;500;600;700&display=swap"
    )
else:
    apply_kw["font_sans"] = "DM Sans"
    apply_kw["font_link"] = (
        "https://fonts.googleapis.com/css2?"
        "family=DM+Sans:wght@400;500;600;700&display=swap"
    )
primary_ov = (st.session_state.demo_primary or "").strip()
if primary_ov:
    apply_kw["primary"] = primary_ov

facade.theme.apply(**apply_kw)

# `st.markdown` `<style>` is easy to strip or lose cascade order; style-only `st.html`
# is routed to Streamlit's event container and reliably global. Caption containers
# use muted body tokens + opacity; sidebar chrome stays dark regardless of Base radio.
st.html(
    """
<style>
    [data-testid="stCaptionContainer"] {
        color: var(--foreground) !important;
        opacity: 1 !important;
    }
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color: var(--chrome-foreground) !important;
    }
    [data-testid="stCaptionContainer"] *:not(a) {
        color: inherit !important;
    }
    [data-testid="stCaptionContainer"] a {
        color: var(--primary) !important;
    }
    /* Streamlit markdown uses `stMarkdownContainer`; façade still targets `stMarkdown`. */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: var(--chrome-foreground) !important;
        opacity: 1 !important;
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] *:not(a) {
        color: inherit !important;
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] a {
        color: var(--primary) !important;
    }
</style>
"""
)

facade.TopBar(title="streamlit-facade playground", user="Demo user", avatar="F")

st.title("streamlit-facade playground")
st.caption(
    "Interactive showcase for "
    "[streamlit-facade](https://github.com/itsdaniyalm/streamlit-facade) "
    "(shadcn-inspired Streamlit components)."
)

col_link1, col_link2, col_link3 = st.columns(3)
with col_link1:
    _facade_link_button_compat(
        "GitHub repo",
        url="https://github.com/itsdaniyalm/streamlit-facade",
        variant="outline",
        icon="external-link",
        css_key="demo_lb_gh",
    )
with col_link2:
    _facade_link_button_compat(
        "PyPI",
        url="https://pypi.org/project/streamlit-facade/",
        variant="ghost",
        size="sm",
        icon="download",
        css_key="demo_lb_pypi",
    )
with col_link3:
    _facade_link_button_compat(
        "Report issue",
        url="https://github.com/itsdaniyalm/streamlit-facade/issues",
        variant="default",
        icon="bug",
        css_key="demo_lb_issue",
    )

(
    tab_theme,
    tab_form,
    tab_display,
    tab_layout,
    tab_data,
    tab_icons,
) = facade.Tabs(
    [
        "Theme & tokens",
        "Form controls",
        "Display",
        "Layout",
        "Data",
        "Icons",
    ]
)

with tab_theme:
    facade.Card(
        title="Applied theme",
        description=(
            f"Sidebar preset `{st.session_state.demo_preset}` → façade tokens from "
            f"`{_effective_preset}`, base `{st.session_state.demo_base}`, "
            f"radius `{st.session_state.demo_radius}`."
            + (
                f" Custom primary `{primary_ov}`."
                if primary_ov
                else ""
            )
        ),
    )
    facade.Alert(
        "Design tokens flow through native Streamlit widgets and facade HTML.",
        title="Token system",
        variant="info",
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        facade.Metric("Requests", "12.4k", delta="8%", delta_color="normal")
    with c2:
        facade.Metric("Errors", "42", delta="-12%", delta_color="inverse")
    with c3:
        facade.Metric("Latency", "120 ms", delta="0%", delta_color="off")

with tab_form:
    r1, r2 = st.columns(2)
    with r1:
        facade.Input(label="Email", placeholder="you@example.com", key="demo_email")
        facade.Textarea(
            label="Notes",
            placeholder="Multi-line text…",
            height=100,
            max_chars=500,
            key="demo_notes",
        )
        picked = facade.Select(
            ["Analytics", "Billing", "Support"],
            label="Department",
            placeholder="Choose…",
            key="demo_select",
        )
        st.caption(f"Select returned: `{picked!r}`")
    with r2:
        facade.Checkbox("Subscribe to updates", value=True, key="demo_chk")
        facade.Radio(
            ["Free", "Pro", "Enterprise"],
            label="Plan",
            horizontal=True,
            key="demo_radio",
        )
        facade.Toggle("Enable beta features", key="demo_toggle")
        vol = facade.Slider(
            "Volume",
            min_value=0,
            max_value=100,
            value=33,
            key="demo_slider",
        )
        st.caption(f"Slider: **{vol}**")

    facade.Separator()
    dcol1, dcol2 = st.columns(2)
    with dcol1:
        facade.DatePicker(
            label="Ship date",
            key="demo_date",
            min_value=datetime.date.today(),
        )
    with dcol2:
        st.write("**Buttons**")
        b1 = facade.Button("Primary", variant="default", icon="save", key="btn_def")
        b2 = facade.Button("Outline", variant="outline", icon="download", key="btn_out")
        b3 = facade.Button("Ghost", variant="ghost", key="btn_gh")
        b4 = facade.Button(
            "Destructive",
            variant="destructive",
            icon="trash",
            key="btn_dest",
        )
        st.caption(
            " — ".join(
                f"{n}: clicked"
                for n, v in [
                    ("Primary", b1),
                    ("Outline", b2),
                    ("Ghost", b3),
                    ("Destructive", b4),
                ]
                if v
            )
            or "Click a button to see feedback here."
        )

    if facade.Button("Show toast notification", icon="bell", key="btn_toast"):
        facade.Toast("Settings saved", icon="check")

    if facade.Button("Run spinner demo", icon="refresh", key="btn_spin"):
        with facade.Spinner("Working…"):
            time.sleep(1.2)
        st.success("Spinner finished.")

with tab_display:
    facade.Alert("Operation completed.", title="Success", variant="success")
    facade.Alert("Check your inputs.", title="Warning", variant="warning")
    facade.Alert("Could not save.", title="Error", variant="error")

    x1, x2, x3 = st.columns(3)
    with x1:
        facade.Badge("Default")
        facade.Badge("Success", variant="success")
    with x2:
        facade.Badge("Warning", variant="warning")
        facade.Badge("Error", variant="error")
    with x3:
        facade.Badge("Outline", variant="outline")
        facade.Badge("Muted", variant="muted")
        facade.Badge(
            "Custom",
            bg_color="#7C3AED",
            text_color="#FFFFFF",
            key="badge_custom",
        )

    facade.Separator(label="Cards")
    ic1, ic2 = st.columns(2)
    with ic1:
        facade.Card(title="Basic card", description="Muted surface with border radius from tokens.")
    with ic2:
        facade.IconCard(
            title="Icon card",
            description="Leading Lucide icon mapped from facade name.",
            icon="sparkle",
            icon_size=28,
        )

with tab_layout:
    facade.Separator(label="Accordion")
    with facade.Accordion("Advanced options", icon="settings"):
        st.write("Hidden until expanded — uses `st.expander` under the hood.")

    facade.Separator(label="StyledContainer")
    for edge in ("all", "top", "left"):
        with facade.StyledContainer(
            border=edge,
            key=f"styled_{edge}",
        ):
            st.markdown(f"Border accent: **`{edge}`** — nested content inherits muted background.")

with tab_data:
    st.markdown("**Progress** — tied to the slider below.")
    pct = st.slider(
        "Completion %",
        min_value=0,
        max_value=100,
        value=62,
        key="demo_progress_pct",
    )
    facade.Progress(value=pct, label="Upload")

    facade.Separator(label="Dataframe")
    df = pd.DataFrame(
        {
            "sku": ["A1", "B2", "C3"],
            "qty": [12, 7, 22],
            "status": ["ok", "hold", "ok"],
        }
    )
    st.dataframe(df, hide_index=True, width="stretch")

with tab_icons:
    st.markdown(
        "`facade.Icon()` renders **Lucide** SVGs by name; use `facade.to_lucide(facade_name)` "
        "when starting from a facade registry name. Buttons use Material via `to_material`."
    )
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:0.5rem;">'
        f'{facade.Icon("circle-check", size=28, color="var(--primary)")}'
        f"<span>Standalone SVG via facade.Icon</span></div>",
        unsafe_allow_html=True,
    )

    st.text_input("Filter icon names", key="demo_icon_filter")
    q = (st.session_state.demo_icon_filter or "").lower().strip()
    all_names = facade.icon_names()
    filtered = [n for n in all_names if q in n.lower()] if q else all_names[:36]
    filtered = filtered[:48]

    st.caption(
        f"Showing {len(filtered)} facade icon names ({len(all_names)} curated aliases → Lucide/Material)."
    )
    grid = st.columns(8)
    for i, name in enumerate(filtered):
        with grid[i % 8]:
            st.markdown(
                facade.Icon(
                    facade.to_lucide(name),
                    size=22,
                    color="var(--foreground)",
                ),
                unsafe_allow_html=True,
            )

    if filtered:
        sample = filtered[0]
        st.code(
            f'to_material("{sample}") -> {facade.to_material(sample)!r}\n'
            f'to_lucide("{sample}") -> {facade.to_lucide(sample)!r}',
            language="python",
        )
