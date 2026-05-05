import streamlit as st
import datetime


def DatePicker(
    label: str = "Select date",
    value=None,
    min_value=None,
    max_value=None,
    disabled: bool = False,
    key: str = None,
):
    """
    Themed date picker component.

    Args:
        label:      Label above the date picker.
        value:      Default date. None defaults to today.
        min_value:  Minimum selectable date.
        max_value:  Maximum selectable date.
        disabled:   Whether the date picker is disabled.
        key:        Unique key for the widget.
    """
    return st.date_input(
        label,
        value=value or datetime.date.today(),
        min_value=min_value,
        max_value=max_value,
        disabled=disabled,
        key=key,
    )