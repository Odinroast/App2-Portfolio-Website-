import pandas as pd
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
st.write(contact_content)

data = pd.read_csv("data.csv", sep=';')
col3, col4 = st.columns(2)
with col3:
    for index, row in data[:11].iterrows():
        st.header(row["title"])

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        print(index)





