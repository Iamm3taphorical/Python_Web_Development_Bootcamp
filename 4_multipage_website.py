import streamlit as st

st.set_page_config(page_title="Multi-page Website")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the home page!")
elif page == "About":
    st.title("About Page")
    st.write("This is the about page.")
elif page == "Contact":
    st.title("Contact Page")
    st.write("Contact us at email@example.com")
