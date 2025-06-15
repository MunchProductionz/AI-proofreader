import streamlit as st
import requests
from forms import proofread_text_manual_input, proofread_text_file_upload
from compare import compare_texts


# --- Title --- #
st.title("AI Proofreader :sunglasses:")

# --- Option selector --- #
mode = st.selectbox("Choose input type:", ["Manual Input", "Upload Document"])

# --- Input state --- #
st.session_state.setdefault("proofread", {})
st.session_state.setdefault("original", {})


# --- Manual Input Form --- #
if mode == "Manual Input":
    with st.form("manual_input_form"):
        st.text_area("Paste text to proofread here", key="input_text", height=200)
        if st.form_submit_button("Proofread"):
            proofread_text_manual_input()  # populates session_state["original"] and ["proofread"]

# --- File Upload Form --- #
elif mode == "Upload Document":
    with st.form("file_input_form"):
        uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "pptx"])
        if st.form_submit_button("Proofread Document") and uploaded_file:
            proofread_text_file_upload(uploaded_file)  # populates session_state["original"] and ["proofread"]


# --- Output Section --- #
if st.session_state.proofread and st.session_state.original:
    st.subheader("Suggested Changes")
    changed_sections = []
    
    # Find sections that have been changed
    for section, corrected in st.session_state.proofread.items():
        original = st.session_state.original.get(section, "")
        if not original.strip():
            continue
        if corrected.strip() != original.strip():
            changed_sections.append((section, original, corrected))

    # If no changes, show a success message, else display the changes
    if not changed_sections:
        st.success("No corrections are needed.")
    else:
        for section, original, corrected in changed_sections:
            with st.expander(f"Section {section}"):
                diff_html = compare_texts(original, corrected)
                st.markdown(diff_html, unsafe_allow_html=True)

        st.subheader("Corrected Version (Combined)")
        full_corrected = "\n\n".join(
            f"[Section {sec}]\n{txt}" for sec, txt in st.session_state.proofread.items()
        )
        st.text_area("Proofread Text", full_corrected, height=300)