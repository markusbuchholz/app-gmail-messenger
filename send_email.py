#Markus Buchholz
#2021
import smtplib, ssl
import streamlit as st


st.title ("WEB Gmail Messenger")
SUBJECT = st.text_input('email subject')

TEXT = st.text_area('area for text email')

sender_email = st.sidebar.text_input('your email')

password = st.sidebar.text_input('your gmail password')

receiver_email = st.sidebar.text_input('receiver email')

def send_email(message, _password, _sender_email, _receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = _sender_email
    receiver_email = _receiver_email
    password = _password
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
            st.text('email sent!')
        except:
            print("could not login or send the mail.")

clicked = st.button('Send email')

if clicked:
  
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
  
    send_email(message, password, sender_email, receiver_email)
