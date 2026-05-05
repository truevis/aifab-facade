"""
facade icon registry — maps facade icon names to Lucide and Material Symbols.
Users always use facade icon names. facade handles the translation internally.
"""

_ICONS = {
    #  facade name       lucide name         material name
    "save":             ("save",             "save"),
    "trash":            ("trash-2",          "delete"),
    "search":           ("search",           "search"),
    "arrow-right":      ("arrow-right",      "arrow_forward"),
    "arrow-left":       ("arrow-left",       "arrow_back"),
    "arrow-up":         ("arrow-up",         "arrow_upward"),
    "arrow-down":       ("arrow-down",       "arrow_downward"),
    "check":            ("circle-check",     "check_circle"),
    "info":             ("info",             "info"),
    "warning":          ("triangle-alert",   "warning"),
    "error":            ("circle-x",         "cancel"),
    "close":            ("x",                "close"),
    "plus":             ("plus",             "add"),
    "minus":            ("minus",            "remove"),
    "edit":             ("pencil",           "edit"),
    "copy":             ("copy",             "content_copy"),
    "download":         ("download",         "download"),
    "upload":           ("upload",           "upload"),
    "settings":         ("settings",         "settings"),
    "user":             ("user",             "person"),
    "users":            ("users",            "group"),
    "home":             ("house",            "home"),
    "mail":             ("mail",             "mail"),
    "bell":             ("bell",             "notifications"),
    "calendar":         ("calendar",         "calendar_today"),
    "clock":            ("clock",            "schedule"),
    "filter":           ("filter",           "filter_alt"),
    "sort":             ("arrow-up-down",    "sort"),
    "refresh":          ("refresh-cw",       "refresh"),
    "logout":           ("log-out",          "logout"),
    "login":            ("log-in",           "login"),
    "eye":              ("eye",              "visibility"),
    "eye-off":          ("eye-off",          "visibility_off"),
    "lock":             ("lock",             "lock"),
    "unlock":           ("lock-open",        "lock_open"),
    "link":             ("link",             "link"),
    "external-link":    ("external-link",    "open_in_new"),
    "menu":             ("menu",             "menu"),
    "grid":             ("grid-2x2",         "grid_view"),
    "list":             ("list",             "list"),
    "chart":            ("bar-chart-2",      "bar_chart"),
    "trending-up":      ("trending-up",      "trending_up"),
    "trending-down":    ("trending-down",    "trending_down"),
    "star":             ("star",             "star"),
    "heart":            ("heart",            "favorite"),
    "flag":             ("flag",             "flag"),
    "tag":              ("tag",              "label"),
    "folder":           ("folder",           "folder"),
    "file":             ("file",             "description"),
    "image":            ("image",            "image"),
    "help":             ("circle-help",      "help"),
    "sparkle":          ("sparkles",         "auto_awesome"),
    "send":             ("send",             "send"),
    "share":            ("share-2",          "share"),
    "print":            ("printer",          "print"),
    "dashboard":        ("layout-dashboard", "dashboard"),
    "notification":     ("bell-ring",        "notification_important"),
    "check-simple":     ("check",            "check"),
    "expand":           ("chevron-down",     "expand_more"),
    "collapse":         ("chevron-up",       "expand_less"),
    "next":             ("chevron-right",    "chevron_right"),
    "prev":             ("chevron-left",     "chevron_left"),
    "more":             ("ellipsis",         "more_horiz"),
    "more-vertical":    ("ellipsis-vertical","more_vert"),
    "zoom-in":          ("zoom-in",          "zoom_in"),
    "zoom-out":         ("zoom-out",         "zoom_out"),
    "fullscreen":       ("maximize",         "fullscreen"),
    "database":         ("database",         "storage"),
    "cloud":            ("cloud",            "cloud"),
    "code":             ("code",             "code"),
    "terminal":         ("terminal",         "terminal"),
    "bug":              ("bug",              "bug_report"),
    "chart-line":       ("chart-line",       "show_chart"),
    "chart-pie":        ("chart-pie",        "pie_chart"),
}


def to_lucide(name: str) -> str:
    """Return the Lucide icon name for a facade icon name."""
    entry = _ICONS.get(name)
    if not entry:
        raise ValueError(
            f"Unknown facade icon: '{name}'. "
            f"Call facade.icon_names() to see all available icons."
        )
    return entry[0]


def to_material(name: str) -> str:
    """Return the Material Symbols string for a facade icon name."""
    entry = _ICONS.get(name)
    if not entry:
        raise ValueError(
            f"Unknown facade icon: '{name}'. "
            f"Call facade.icon_names() to see all available icons."
        )
    return f":material/{entry[1]}:"


def icon_names() -> list:
    """Return a sorted list of all available facade icon names."""
    return sorted(_ICONS.keys())