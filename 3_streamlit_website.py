import streamlit as st

st.set_page_config(page_title="My Streamlit App", page_icon="🌟")

st.title("Welcome to my Simple Streamlit Website")
st.write("This is a simple website built with Streamlit and Python.")
st.write("My name is Mahir Dyan and I am currently exploring this new framework")
st.write("this is very easy to use and didn't took me much time to grasph it")
st.write("at the moment doing hard code but sooner will start to implement proper projects using this")

name = st.text_input("What is your name?")
if name:
    st.write(f"Hello, {name}!")