
from typing import Any
import numpy as np
import streamlit as st
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFium2Loader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOpenAI
from langchain.globals import set_verbose, set_debug
#import openai
import os

os.environ["OPENAI_API_KEY"] ="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"

set_debug(True)
set_verbose(True)

def loadPDFasDoc(file):
    loader = PyPDFium2Loader(file)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(pages)
    return docs

def queryLLM(docs, prompt_template):
    prompt = PromptTemplate.from_template(prompt_template)
    
    # Define LLM chain
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
    response = stuff_chain.run(docs)

    st.write("Prompt: " + prompt_template)
    st.write("Response: " + response)


summary_prompt = """Write a summary for each of the following elements: contract term, royalty rates, termination conditions and reporting obligations in the following text:
"{text}"
CONCISE SUMMARY:"""

penalty_prompt = """Summarize the penalty fees mentioned in the following contract:
"{text}"
CONCISE SUMMARY:"""

#docs = loadPDFasDoc("SAMPLE No EQUITY EXCL For Posting 7.17.18.pdf")
#queryLLM(docs, summary_prompt)



def chat() -> None:
    uploaded_file = st.file_uploader(
        "Upload a pdf, docx, or txt file",
        type=["pdf", "docx", "txt"],
        help="Scanned documents are not supported yet!",
    )

    if uploaded_file is not None:
        st.success("Thanks for your file!")
        d = loadPDFasDoc(uploaded_file)
        st.write(d)
    


st.set_page_config(page_title="Contract Q&A", page_icon="📹")
st.markdown("# Contract Q&A")
st.sidebar.header("Contract Q&A")
st.write(
    """With this app you can Q&A your contract."""
)

chat()

