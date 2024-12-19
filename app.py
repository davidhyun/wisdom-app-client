import streamlit as st
from routes.home import home
from routes.quotes import quotes

st.set_page_config(page_title="With Wisdom", page_icon="💬", layout="wide")
st.sidebar.title("메뉴 선택")
page = st.sidebar.radio("메뉴 이동", ["Home", "Quotes"])

if page == "Home":
    home()
elif page == "Quotes":
    quotes()