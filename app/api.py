import streamlit as st
import requests


def call_api(text: str) -> dict:
    """Call API and return the corrected text."""
    response = requests.post("http://localhost:8000/proofread", json={"text": text})
    return response.json()