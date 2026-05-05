import streamlit as st
from contextlib import contextmanager


@contextmanager
def Accordion(
    label: str,
    expanded: bool = False,
    icon: str = None,
):
    """
    Themed accordion / expander component.

    Args:
        label:    Header label text.
        expanded: Whether the accordion is open by default.
        icon:     Optional facade icon name e.g. "settings", "user"
        
    Usage:
        with facade.Accordion("Section title"):
            st.write("Content inside")
    """
    from ..icons import to_material
    material_icon = to_material(icon) if icon else None

    with st.expander(label, expanded=expanded, icon=material_icon):
        yield