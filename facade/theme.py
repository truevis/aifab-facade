import streamlit as st
import os

_RADIUS_MAP = {"xxs": "0.1rem", "sm": "0.25rem", "md": "0.5rem", "lg": "0.75rem", "xl": "1rem"}

_PRESETS = {
    "default": {
        "primary":            "#1059A0",
        "primary_foreground": "#FFFFFF",
        "background":         "#FFFFFF",
        "foreground":         "#0F172A",
        "muted":              "#F1F5F9",
        "muted_foreground":   "#64748B",
        "border":             "#E2E8F0",
        "destructive":        "#EF4444",
        "chrome_background":  "#1059A0",
        "chrome_foreground":  "#E8EDF2",
        "chrome_border":      "#1E6FBE",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "default-dark": {
        "primary":            "#3B82F6",
        "primary_foreground": "#FFFFFF",
        "background":         "#0F172A",
        "foreground":         "#E2E8F0",
        "muted":              "#1E293B",
        "muted_foreground":   "#94A3B8",
        "border":             "#334155",
        "destructive":        "#EF4444",
        "chrome_background":  "#020817",
        "chrome_foreground":  "#E2E8F0",
        "chrome_border":      "#1E293B",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "carbon-sage": {
        "primary":            "#8FAF3D",
        "primary_foreground": "#FFFFFF",
        "background":         "#F7F7F5",
        "foreground":         "#1A1A18",
        "muted":              "#EEEDE9",
        "muted_foreground":   "#6B6A65",
        "border":             "#DDDCD7",
        "destructive":        "#F43F5E",
        "chrome_background":  "#1A1A18",
        "chrome_foreground":  "#E8E8E4",
        "chrome_border":      "#2A2A27",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "carbon-sage-dark": {
        "primary":            "#A3C44A",
        "primary_foreground": "#0A0A08",
        "background":         "#0A0A08",
        "foreground":         "#F5F5F3",
        "muted":              "#1A1A18",
        "muted_foreground":   "#8B8A85",
        "border":             "#2A2A27",
        "destructive":        "#F43F5E",
        "chrome_background":  "#111110",
        "chrome_foreground":  "#F5F5F3",
        "chrome_border":      "#1A1A18",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "carbon-light": {
        "primary":            "#CDEA12",
        "primary_foreground": "#0A0A08",
        "background":         "#F5F5F3",
        "foreground":         "#0A0A08",
        "muted":              "#EBEBEA",
        "muted_foreground":   "#6B6A65",
        "border":             "#DDDCDA",
        "destructive":        "#F43F5E",
        "chrome_background":  "#0A0A08",
        "chrome_foreground":  "#F5F5F3",
        "chrome_border":      "#1A1A18",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "carbon-dark": {
        "primary":            "#CDEA12",
        "primary_foreground": "#0A0A08",
        "background":         "#0A0A08",
        "foreground":         "#F5F5F3",
        "muted":              "#1A1A18",
        "muted_foreground":   "#8B8A85",
        "border":             "#2A2A27",
        "destructive":        "#F43F5E",
        "chrome_background":  "#111110",
        "chrome_foreground":  "#F5F5F3",
        "chrome_border":      "#2A2A27",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "carbon-amber": {
        "primary":            "#F59E0B",
        "primary_foreground": "#0A0F0E",
        "background":         "#F7F7F5",
        "foreground":         "#1A1A18",
        "muted":              "#EEEDE9",
        "muted_foreground":   "#6B6A65",
        "border":             "#DDDCD7",
        "destructive":        "#F43F5E",
        "chrome_background":  "#1A1A18",
        "chrome_foreground":  "#E8E8E4",
        "chrome_border":      "#2A2A27",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "burgundy": {
        "primary":            "#B8860B",
        "primary_foreground": "#FAF7F2",
        "background":         "#FAF7F2",
        "foreground":         "#1A0A0F",
        "muted":              "#EDE8E0",
        "muted_foreground":   "#8B6F72",
        "border":             "#DDD5C8",
        "destructive":        "#9B2335",
        "chrome_background":  "#4A0E20",
        "chrome_foreground":  "#FAF7F2",
        "chrome_border":      "#6B1530",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "minimal": {
        "primary":            "#18181B",
        "primary_foreground": "#FFFFFF",
        "background":         "#FFFFFF",
        "foreground":         "#09090B",
        "muted":              "#F4F4F5",
        "muted_foreground":   "#71717A",
        "border":             "#E4E4E7",
        "destructive":        "#EF4444",
        "chrome_background":  "#18181B",
        "chrome_foreground":  "#F4F4F5",
        "chrome_border":      "#27272A",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.25rem",
    },
    "warm": {
        "primary":            "#D97706",
        "primary_foreground": "#FFFFFF",
        "background":         "#FFFBF5",
        "foreground":         "#1C1917",
        "muted":              "#FEF3C7",
        "muted_foreground":   "#78716C",
        "border":             "#E7E5E4",
        "destructive":        "#EF4444",
        "chrome_background":  "#92400E",
        "chrome_foreground":  "#FEF3C7",
        "chrome_border":      "#B45309",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.75rem",
    },
    "dark": {
        "primary":            "#3B82F6",
        "primary_foreground": "#FFFFFF",
        "background":         "#0F172A",
        "foreground":         "#E2E8F0",
        "muted":              "#1E293B",
        "muted_foreground":   "#94A3B8",
        "border":             "#334155",
        "destructive":        "#EF4444",
        "chrome_background":  "#020817",
        "chrome_foreground":  "#E2E8F0",
        "chrome_border":      "#1E293B",
        "font_sans":          "system-ui",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
    "daniyal": {
        "primary":            "#10274A",
        "primary_foreground": "#FFFFFF",
        "background":         "#F5F7FB",
        "foreground":         "#1C1917",
        "muted":              "#FFFFFF",
        "muted_foreground":   "#184185",
        "border":             "#E2E8F0",
        "destructive":        "#AF3280",
        "chrome_background":  "#10274A",
        "chrome_foreground":  "#E8EDF2",
        "chrome_border":      "#184185",
        "font_sans":          "DM Sans",
        "font_mono":          "monospace",
        "radius":             "0.5rem",
    },
}


def _write_config(preset_name: str, tokens: dict, base: str = None) -> bool:
    if base is not None:
        resolved_base = base
    else:
        is_dark = preset_name in ("dark", "default-dark", "carbon-dark", "carbon-sage-dark") or tokens["background"].lower() in (
            "#0f172a", "#1e1e2e", "#1e293b", "#111827", "#09090b", "#0a0a08",
        )
        resolved_base = "dark" if is_dark else "light"

    config_dir  = ".streamlit"
    config_path = os.path.join(config_dir, "config.toml")
    os.makedirs(config_dir, exist_ok=True)

    content = (
        f'[theme]\n'
        f'base = "{resolved_base}"\n'
        f'primaryColor = "{tokens["primary"]}"\n'
        f'backgroundColor = "{tokens["background"]}"\n'
        f'secondaryBackgroundColor = "{tokens["muted"]}"\n'
        f'textColor = "{tokens["foreground"]}"\n'
    )

    existing = ""
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            existing = f.read()

    if existing != content:
        with open(config_path, "w") as f:
            f.write(content)
        return True

    return False


def apply(
    preset: str = "default",
    base: str = None,
    primary: str = None,
    primary_foreground: str = None,
    background: str = None,
    foreground: str = None,
    muted: str = None,
    muted_foreground: str = None,
    border: str = None,
    destructive: str = None,
    chrome_background: str = None,
    chrome_foreground: str = None,
    chrome_border: str = None,
    font_sans: str = None,
    font_mono: str = None,
    font_link: str = None,
    radius: str = None,
):
    tokens = dict(_PRESETS.get(preset, _PRESETS["default"]))

    overrides = {
        "primary":            primary,
        "primary_foreground": primary_foreground,
        "background":         background,
        "foreground":         foreground,
        "muted":              muted,
        "muted_foreground":   muted_foreground,
        "border":             border,
        "destructive":        destructive,
        "chrome_background":  chrome_background,
        "chrome_foreground":  chrome_foreground,
        "chrome_border":      chrome_border,
        "font_sans":          font_sans,
        "font_mono":          font_mono,
        "radius":             radius,
    }
    for k, v in overrides.items():
        if v is not None:
            tokens[k] = _RADIUS_MAP.get(v, v) if k == "radius" else v

    changed = _write_config(preset, tokens, base=base)
    if changed:
        st.rerun()

    font_tag = f'<link href="{font_link}" rel="stylesheet">' if font_link else ""

    css_vars = (
        f"--primary: {tokens['primary']};\n"
        f"            --primary-foreground: {tokens['primary_foreground']};\n"
        f"            --background: {tokens['background']};\n"
        f"            --foreground: {tokens['foreground']};\n"
        f"            --muted: {tokens['muted']};\n"
        f"            --muted-foreground: {tokens['muted_foreground']};\n"
        f"            --border: {tokens['border']};\n"
        f"            --destructive: {tokens['destructive']};\n"
        f"            --chrome-background: {tokens['chrome_background']};\n"
        f"            --chrome-foreground: {tokens['chrome_foreground']};\n"
        f"            --chrome-border: {tokens['chrome_border']};\n"
        f"            --font-sans: {tokens['font_sans']};\n"
        f"            --font-mono: {tokens['font_mono']};\n"
        f"            --radius: {tokens['radius']};"
    )

    css = """
        <style>
            :root {
                """ + css_vars + """
            }

            /* ── Streamlit header ── */
            header[data-testid="stHeader"] {
                background-color: var(--background) !important;
                border-bottom: none !important;
                box-shadow: none !important;
            }
            div[data-testid="stToolbar"] {
                background-color: var(--background) !important;
            }
            #stDecoration {
                display: none !important;
            }

            /* ── App background ── */
            .stApp, body {
                background-color: var(--background) !important;
            }

            /* ── Top padding ── */
            .stMainBlockContainer {
                padding-top: 2.5rem !important;
                padding-bottom: 2rem !important;
                padding-left: 2rem !important;
                padding-right: 2rem !important;
            }

            /* ── Typography — never touch span (icon fonts live there) ── */
            html, body {
                font-family: var(--font-sans) !important;
            }
            h1, h2, h3, h4, h5, h6 {
                font-family: var(--font-sans) !important;
                color: var(--foreground) !important;
            }
            div[data-testid="stHeading"] p,
            div[data-testid="stHeading"] h1,
            div[data-testid="stHeading"] h2,
            div[data-testid="stHeading"] h3 {
                font-family: var(--font-sans) !important;
                color: var(--foreground) !important;
            }
            div[data-testid="stText"] p,
            div[data-testid="stMarkdown"] p {
                font-family: var(--font-sans) !important;
                color: var(--foreground) !important;
            }
            label {
                font-family: var(--font-sans) !important;
            }

            /* ── Tighten vertical spacing ── */
            div[data-testid="stVerticalBlock"] {
                gap: 0.75rem !important;
            }
            div[data-testid="stVerticalBlock"] > div {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stElementContainer"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stElementContainer"] > div {
                margin: 0 !important;
                padding: 0 !important;
            }

            /* ── Buttons ── */
            div[data-testid="stButton"] {
                width: fit-content !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stButton"] > button {
                min-width: 6rem !important;
                width: auto !important;
                margin: 0 !important;
                border-radius: var(--radius) !important;
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                transition: opacity 0.15s, background 0.15s !important;
            }

            /* ── Text inputs ── */
            div[data-testid="stTextInput"] {
                margin-bottom: 0 !important;
            }
            div[data-testid="stTextInput"] [data-baseweb="input"] {
                border-width: 1px !important;
                border-style: solid !important;
                border-color: var(--border) !important;
                border-radius: var(--radius) !important;
                background-color: var(--muted) !important;
                box-shadow: none !important;
                outline: none !important;
            }
            div[data-testid="stTextInput"] [data-baseweb="input"]:focus-within {
                border-color: var(--primary) !important;
                box-shadow: 0 0 0 2px color-mix(in srgb, var(--primary) 25%, transparent) !important;
            }
            div[data-testid="stTextInput"] [data-baseweb="base-input"] input {
                border: none !important;
                outline: none !important;
                box-shadow: none !important;
                background: transparent !important;
                color: var(--foreground) !important;
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
            }
            div[data-testid="stTextInput"] label {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                color: var(--foreground) !important;
                margin-bottom: 0.25rem !important;
            }

            /* ── Textarea ── */
            div[data-testid="stTextArea"] {
                margin-bottom: 0 !important;
                margin-top: 0.25rem !important;
            }
            div[data-testid="stTextArea"] [data-baseweb="textarea"] {
                border-width: 1px !important;
                border-style: solid !important;
                border-color: var(--border) !important;
                border-radius: var(--radius) !important;
                background-color: var(--muted) !important;
                box-shadow: none !important;
                outline: none !important;
            }
            div[data-testid="stTextArea"] [data-baseweb="textarea"]:focus-within {
                border-color: var(--primary) !important;
                box-shadow: 0 0 0 2px color-mix(in srgb, var(--primary) 25%, transparent) !important;
            }
            div[data-testid="stTextArea"] textarea {
                border: none !important;
                outline: none !important;
                box-shadow: none !important;
                background: transparent !important;
                color: var(--foreground) !important;
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
            }
            div[data-testid="stTextArea"] label {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                color: var(--foreground) !important;
                margin-bottom: 0.25rem !important;
            }

            /* ── Checkbox ── */
            div[data-testid="stCheckbox"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stCheckbox"] label {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                color: var(--foreground) !important;
                gap: 0.5rem !important;
            }
            div[data-testid="stCheckbox"] label span[data-baseweb="checkbox"] {
                background-color: var(--muted) !important;
                border-width: 1px !important;
                border-style: solid !important;
                border-color: var(--border) !important;
                border-radius: calc(var(--radius) * 0.5) !important;
            }
            div[data-testid="stCheckbox"] label[aria-checked="true"] span[data-baseweb="checkbox"] {
                background-color: var(--primary) !important;
                border-color: var(--primary) !important;
            }
            div[data-testid="stCheckbox"] label[aria-checked="true"] span[data-baseweb="checkbox"] svg path {
                fill: var(--primary-foreground) !important;
            }

            /* ── Radio ── */
            div[data-testid="stRadio"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stRadio"] label {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                color: var(--foreground) !important;
            }
            div[data-testid="stRadio"] > label {
                font-weight: 500 !important;
                margin-bottom: 0.25rem !important;
            }
            div[data-testid="stRadio"] label span[data-baseweb="radio"] {
                background-color: var(--muted) !important;
                border-width: 1px !important;
                border-style: solid !important;
                border-color: var(--border) !important;
            }
            div[data-testid="stRadio"] label[aria-checked="true"] span[data-baseweb="radio"] {
                background-color: var(--primary) !important;
                border-color: var(--primary) !important;
            }
            div[data-testid="stRadio"] label[aria-checked="true"] span[data-baseweb="radio"] div {
                background-color: var(--primary-foreground) !important;
            }

            /* ── Toggle ── */
            div[data-testid="stToggle"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stToggle"] label {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                color: var(--foreground) !important;
                gap: 0.5rem !important;
            }
            div[data-testid="stToggle"] label span[data-baseweb="toggle"] {
                background-color: var(--border) !important;
            }
            div[data-testid="stToggle"] label[aria-checked="true"] span[data-baseweb="toggle"] {
                background-color: var(--primary) !important;
            }

            /* ── Slider ── */
            div[data-testid="stSlider"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stSlider"] label {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                color: var(--foreground) !important;
                margin-bottom: 0.25rem !important;
            }
            div[data-testid="stSlider"] [data-testid="stThumbValue"] {
                font-family: var(--font-sans) !important;
                font-size: 0.8rem !important;
                color: var(--muted-foreground) !important;
            }
            div[data-testid="stSlider"] [data-testid="stTickBarMin"],
            div[data-testid="stSlider"] [data-testid="stTickBarMax"] {
                font-family: var(--font-sans) !important;
                font-size: 0.8rem !important;
                color: var(--muted-foreground) !important;
            }
            div[data-testid="stSlider"] [data-testid="stThumbValue"] *,
            div[data-testid="stSlider"] [data-testid="stTickBarMin"] *,
            div[data-testid="stSlider"] [data-testid="stTickBarMax"] * {
                font-family: var(--font-sans) !important;
                font-size: 0.8rem !important;
            }
            div[data-testid="stSlider"] [role="slider"] {
                background-color: var(--primary) !important;
                border-color: var(--primary) !important;
            }
            div[data-testid="stSlider"] [data-testid="stSliderTrack"] > div:first-child {
                background-color: var(--border) !important;
            }
            div[data-testid="stSlider"] [data-testid="stSliderTrack"] > div:nth-child(2) {
                background-color: var(--primary) !important;
            }

            /* ── DatePicker ── */
            div[data-testid="stDateInput"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stDateInput"] label {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                color: var(--foreground) !important;
                margin-bottom: 0.25rem !important;
            }
            div[data-testid="stDateInput"] [data-baseweb="input"] {
                border-width: 1px !important;
                border-style: solid !important;
                border-color: var(--border) !important;
                border-radius: var(--radius) !important;
                background-color: var(--muted) !important;
                box-shadow: none !important;
            }
            div[data-testid="stDateInput"] [data-baseweb="input"]:focus-within {
                border-color: var(--primary) !important;
                box-shadow: 0 0 0 2px color-mix(in srgb, var(--primary) 25%, transparent) !important;
            }
            div[data-testid="stDateInput"] [data-baseweb="base-input"] input {
                border: none !important;
                outline: none !important;
                box-shadow: none !important;
                background: transparent !important;
                color: var(--foreground) !important;
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
            }

            /* ── Metric ── */
            div[data-testid="stMetric"] {
                background-color: var(--muted) !important;
                border: 1px solid var(--border) !important;
                border-radius: var(--radius) !important;
                padding: 1rem 1.25rem !important;
                width: 100% !important;
                box-sizing: border-box !important;
                overflow: visible !important;
            }
            div[data-testid="stElementContainer"]:has(div[data-testid="stMetric"]) {
                overflow: visible !important;
                padding: 2px !important;
            }
            div[data-testid="stMetricLabel"] {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                color: var(--muted-foreground) !important;
            }
            div[data-testid="stMetricLabel"] p {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                color: var(--muted-foreground) !important;
            }
            div[data-testid="stMetricValue"] {
                font-family: var(--font-sans) !important;
                font-size: 2rem !important;
                font-weight: 600 !important;
                color: var(--foreground) !important;
            }
            div[data-testid="stMetricValue"] p {
                font-family: var(--font-sans) !important;
                font-size: 2rem !important;
                font-weight: 600 !important;
                color: var(--foreground) !important;
            }
            div[data-testid="stMetricDelta"] {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
            }
            div[data-testid="stMetricDelta"] svg {
                width: 1rem !important;
                height: 1rem !important;
            }

            /* ── Columns ── */
            div[data-testid="stColumn"] {
                padding-left: 0.5rem !important;
                padding-right: 0.5rem !important;
            }

            /* ── Tabs ── */
            div[data-testid="stTabs"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stTabs"] [data-testid="stTabBar"] {
                background-color: var(--background) !important;
                border-bottom: 1px solid var(--border) !important;
                gap: 0 !important;
            }
            div[data-testid="stTabs"] button[role="tab"] {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                color: var(--muted-foreground) !important;
                border: none !important;
                border-bottom: 2px solid transparent !important;
                background: transparent !important;
                padding: 0.5rem 1rem !important;
                border-radius: 0 !important;
                transition: color 0.15s !important;
            }
            div[data-testid="stTabs"] button[role="tab"]:hover {
                color: var(--foreground) !important;
                background: transparent !important;
            }
            div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
                color: var(--primary) !important;
                border-bottom: 2px solid var(--primary) !important;
                background: transparent !important;
            }
            div[data-testid="stTabs"] [data-testid="stTabPanel"] {
                padding-top: 1rem !important;
            }

            /* ── Progress ── */
            div[data-testid="stProgress"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            div[data-testid="stProgress"] > div {
                background-color: var(--border) !important;
                border-radius: 9999px !important;
                height: 0.5rem !important;
            }
            div[data-testid="stProgress"] > div > div {
                background-color: var(--primary) !important;
                border-radius: 9999px !important;
            }

            /* ── DataFrame ── */
            div[data-testid="stDataFrame"] {
                border: 1px solid var(--border) !important;
                border-radius: var(--radius) !important;
                overflow: hidden !important;
            }
            div[data-testid="stDataFrame"] [data-testid="glideDataEditor"] {
                font-family: var(--font-sans) !important;
            }
            div[data-testid="stDataFrame"] canvas {
                border-radius: var(--radius) !important;
            }

            /* ── Accordion ── */
            div[data-testid="stExpander"] {
                border: 1px solid var(--border) !important;
                border-radius: var(--radius) !important;
                background: var(--muted) !important;
                overflow: hidden !important;
                margin: 0 !important;
            }
            div[data-testid="stExpander"] summary {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                color: var(--foreground) !important;
                padding: 0.75rem 1rem !important;
                background: var(--muted) !important;
            }
            div[data-testid="stExpander"] summary:hover {
                background: var(--border) !important;
            }
            div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
                border-top: 1px solid var(--border) !important;
                padding: 1rem !important;
            }

            /* ── Selectbox ── */
            div[data-testid="stSelectbox"] {
                margin-bottom: 0 !important;
            }
            div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
                border-width: 1px !important;
                border-style: solid !important;
                border-color: var(--border) !important;
                border-radius: var(--radius) !important;
                background-color: var(--muted) !important;
                color: var(--foreground) !important;
                box-shadow: none !important;
                outline: none !important;
            }
            div[data-testid="stSelectbox"] label {
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 500 !important;
                color: var(--foreground) !important;
            }

            /* ── Sidebar ── */
            [data-testid="stSidebar"] {
                background-color: var(--chrome-background) !important;
                border-right: 1px solid var(--chrome-border) !important;
            }
            [data-testid="stSidebar"] p,
            [data-testid="stSidebar"] label,
            [data-testid="stSidebar"] h1,
            [data-testid="stSidebar"] h2,
            [data-testid="stSidebar"] h3 {
                color: var(--chrome-foreground) !important;
                font-family: var(--font-sans) !important;
            }
            [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] {
                gap: 0.125rem !important;
            }
            [data-testid="stSidebar"] div[data-testid="stElementContainer"] {
                margin: 0 !important;
                padding: 0 !important;
            }
            [data-testid="stSidebar"] .stButton {
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            [data-testid="stSidebar"] .stButton button {
                background: transparent !important;
                border: none !important;
                border-radius: var(--radius) !important;
                color: var(--chrome-foreground) !important;
                font-family: var(--font-sans) !important;
                font-size: 0.875rem !important;
                font-weight: 400 !important;
                text-align: left !important;
                justify-content: flex-start !important;
                padding: 0.5rem 1rem !important;
                width: 100% !important;
                min-width: unset !important;
                box-shadow: none !important;
            }
            [data-testid="stSidebar"] .stButton button:hover {
                background: rgba(255,255,255,0.08) !important;
            }
            [data-testid="stSidebar"] .stButton button p {
                text-align: left !important;
                width: 100% !important;
                color: var(--chrome-foreground) !important;
            }

            /* ── Collapse button ── */
            [data-testid="collapsedControl"] {
                position: fixed !important;
                top: 1rem !important;
                left: 0.6rem !important;
                z-index: 999 !important;
            }

        </style>
    """

    st.markdown(font_tag + css, unsafe_allow_html=True)