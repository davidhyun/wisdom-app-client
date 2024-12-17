import streamlit as st
from services.api import get_quote_by_id


def quotes():
    st.title("Famous Quotes")
    quote_id = st.text_input("명언ID", "숫자 입력하세요")
    
    quotes = get_quote_by_id(quote_id)
    if quotes:
        st.write(quotes)
    else:
        st.error("No quote found.")