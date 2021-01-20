#Markus Buchholz
#2021
import smtplib, ssl
import streamlit as st
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os


st.title ("WEB Gmail Messenger !")
SUBJECT = st.text_input('email subject')

TEXT = st.text_area('area for text email')

sender_email = st.sidebar.text_input('your email')

password = st.sidebar.text_input('your gmail password')

receiver_email = st.sidebar.text_input('receiver email')

user_attachment = st.file_uploader('File uploader')

def send_email(sender_email,receiver_email, SUBJECT, TEXT, password, user_attachment ):
    #print(user_attachment.name)
    msg = MIMEMultipart() 
    msg['From'] = sender_email 
    msg['To'] = receiver_email 
    msg['Subject'] = SUBJECT
    body = TEXT
  

    msg.attach(MIMEText(body, 'plain')) 
    
    filename = user_attachment.name #"File_name_with_extension"
    #attachment = open(user_attachment, "rb")
    attachment = user_attachment 
    
    p = MIMEBase('application', 'octet-stream') 
    
    p.set_payload((attachment).read()) 
    
    encoders.encode_base64(p) 
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
    msg.attach(p) 

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(sender_email, password)
        text = msg.as_string() 
        s.sendmail(sender_email, receiver_email, text)
        print('email sent!')
        st.text('email sent!')
        s.quit() 
    except:
        print("could not login or send the mail.")

clicked = st.button('Send email')

if clicked:
  
  
    send_email(sender_email,receiver_email, SUBJECT, TEXT, password, user_attachment)
