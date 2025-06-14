import streamlit as st
from api import call_api


def proofread_text() -> None:
    """Proofread the text entered in the input form."""
    
    text = st.session_state.input_text
    if not text:
        st.session_state.proofread = "Please enter some text to proofread."
        return
    
    response = call_api(text)
    if response.get("result") == "Success":
        st.session_state.proofread = response.get("proofread_text")
        st.session_state.original = text
    else:
        st.session_state.proofread = f"Error: {response.get('error_msg')}"