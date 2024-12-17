import streamlit as st
from routes.home import home
from routes.quotes import quotes

st.set_page_config(page_title="Quotes App", page_icon="💬", layout="wide")

# 사이드바 라우팅
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Quotes", "Upload Quote", "About"])

if page == "Home":
    home()
elif page == "Quotes":
    quotes()