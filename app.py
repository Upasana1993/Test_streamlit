import streamlit as st

st.title("Hello, World!")
st.write("This is my first Streamlit app 🚀")

name = st.text_input("What's your name?")
if name:
    st.success(f"Welcome, {name}!")
