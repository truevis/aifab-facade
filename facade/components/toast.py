import streamlit as st
from ..icons import to_material


def Toast(
    message: str,
    icon: str = None,
    duration: int = 4,
):
    """
    Themed toast notification.

    Args:
        message:  Text to display in the toast.
        icon:     Optional facade icon name e.g. "check", "error", "warning"
        duration: How long the toast is displayed in seconds (default 4).

    Usage:
        facade.Toast("Saved!", icon="check")
    """
    material_icon = to_material(icon) if icon else None

    st.toast(
        message,
        icon=material_icon,
    )