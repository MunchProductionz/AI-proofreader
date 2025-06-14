import streamlit as st
import requests
from forms import proofread_text
from redlines import Redlines

# --- Title --- #
st.title("My first app :sunglasses:")

# --- Initialize session state once --- #
st.session_state.setdefault("proofread", None)
st.session_state.setdefault("original", None)

# --- API Call Function --- #
with st.form("input_form"):
    st.text_area("Paste text to proofread here", key="input_text", height=200)
    st.form_submit_button("Proofread", on_click=proofread_text)

if st.session_state.proofread is not None and st.session_state.original is not None:
    st.subheader("Suggested Changes")

    redlined = Redlines(st.session_state.original, st.session_state.proofread)
    diff_html = redlined.output_markdown  # or use `output_html`

    st.markdown(diff_html, unsafe_allow_html=True)

    st.subheader("Corrected Version")
    st.write(st.session_state.proofread)
            
