import pandas
import streamlit as st


st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jaime Motta")
    content = """
    Hi, I am Jaime! I am a Python programmer, I graduated from computer science.
    """
    st.write(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_column , col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
1
with col4:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

