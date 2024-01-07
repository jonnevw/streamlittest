
from typing import Any

import numpy as np

import streamlit as st


def chat() -> None:
    uploaded_file = st.file_uploader(
        "Upload a pdf, docx, or txt file",
        type=["pdf", "docx", "txt"],
        help="Scanned documents are not supported yet!",
    )
    


st.set_page_config(page_title="Contract Q&A", page_icon="📹")
st.markdown("# Contract Q&A")
st.sidebar.header("Contract Q&A")
st.write(
    """With this app you can Q&A your contract."""
)

chat()

