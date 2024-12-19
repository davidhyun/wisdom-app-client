import streamlit as st
from services.api import get_quote_by_id
import random

def quotes():
    st.title("명언 자판기")
    if st.button("명언 뽑기"):
        quote_id = random.randint(1, 100)
        quote_id = 1
        quote = get_quote_by_id(quote_id)
        st.markdown(f"""
            ### {quote['content']}
            #### {quote['author_title']} - {quote['author_name']}
        """)