import streamlit as st


def Slider(
    label: str,
    min_value=0,
    max_value=100,
    value=50,
    step=1,
    disabled: bool = False,
    key: str = None,
):
    """
    Themed slider component.

    Args:
        label:      Label above the slider.
        min_value:  Minimum value.
        max_value:  Maximum value.
        value:      Default value. Pass a tuple (min, max) for a range slider.
        step:       Step increment.
        disabled:   Whether the slider is disabled.
        key:        Unique key for the widget.
    """
    return st.slider(
        label,
        min_value=min_value,
        max_value=max_value,
        value=value,
        step=step,
        disabled=disabled,
        key=key,
    )