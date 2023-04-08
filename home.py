import pandas
import streamlit as st


st.set_page_config(layout='wide')
col1, empty_column , col2 = st.columns([0.5, 0.2, 2])


with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jaime Motta")
    content = """
    Hi, I Am Jaime Motta a computer science engineer. Programming is my passion, I am currently working with python 
    developing web applications. I Am still discovering all the benefits that python provides as a programming language 
    compared to my past experiences using c#, c++, Java.
    I like the idea of exploring the wide range of applications that can be implemented safely, quickly and easily in 
    this language.
    
    I will continue experimenting and expanding the variety of applications available in the following list.
    """
    st.write(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!

some of the following applications were created with the guidance of third parties.
"""
st.write(content2)

col3, empty_column, col4 = st.columns([1.2, 0.5, 1.2])

df = pandas.read_csv("data.csv", sep=";")
middlevalue = int(len(df.index)/2)

with col3:
    for index, row in df[middlevalue:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[:middlevalue].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

