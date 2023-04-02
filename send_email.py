import smtplib
import ssl
import os
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "itmandjango@gmail.com"
    #to be use when the deploy is local
    # password = os.getenv("portfolio_password")

    # to be use when the deploy is on streamlit community
    password = st.secrets["EM_PWD"]


    receiver = "itmanco@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
