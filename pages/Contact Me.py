import streamlit as st

st.header("Contact Me")

with st.form(key="form_email", clear_on_submit=True):
    user_email = st.text_input("Enter your email", key="usr_email")
    message = st.text_area("Your Message", key="usr_msg")
    button = st.form_submit_button('Submit')
    if button:
        
