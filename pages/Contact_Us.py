import streamlit as st


st.header("Contact Me")

with st.form(key="email_form"):
    user_mail = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        message = user_mail