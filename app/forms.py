import streamlit as st
from api import call_api
from extraction import extract_text_by_type
import requests


def proofread_text_manual_input() -> None:
    """Proofread the text entered in the input form."""
    text = st.session_state.input_text
    if not text:
        st.session_state.proofread = "Please enter some text to proofread."
        return
    
    response = call_api(text)
    if response.get("result") == "Success":
        page = 0
        st.session_state.proofread[page] = response.get("proofread_text")
        st.session_state.original[page] = text
    else:
        st.session_state.proofread = f"Error: {response.get('error_msg')}"
        

def proofread_text_file_upload(uploaded_file) -> None:
    """Proofread the text extracted from the uploaded file."""
    filetype = uploaded_file.name.split(".")[-1].lower()
    text_sections = extract_text_by_type(uploaded_file, filetype)
    
    st.session_state.original = text_sections
    for page, content in text_sections.items():
        if not content.strip():
            continue
        response = call_api(content)
        if response.get("result") == "Success":
            st.session_state.proofread[page] = response.get("proofread_text")
        else:
            st.session_state.proofread[page] = f"Error: {response.get('error_msg')}"