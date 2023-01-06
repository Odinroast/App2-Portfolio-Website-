import streamlit
import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ruthvick Bandaru")
    content = """
    Hello, My name is Ruthvick Bandaru, Not too much to say rn, wanna play SOT 
    """
    st.info(content)

contact_content = """
Below you can find some of the apps that I have built in python, Feel free to contact me!
"""
streamlit.write(contact_content)

