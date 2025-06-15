import streamlit as st
from redlines import Redlines


def compare_texts(original, corrected):
    """
    Compare two texts and return the differences in a redlined format.
    """
    redlined = Redlines(original, corrected)
    diff_html = redlined.output_markdown  # or use `output_html`
    return diff_html