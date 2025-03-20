import streamlit as sl
from pages.sending_emails import send_email

sl.header('Contact Us')
with sl.form(key='email_form'):
    user_email = sl.text_input('Your email: ')
    raw_message = sl.text_area('Your message: ')
    message = f'''\
Subject: From {user_email}
{raw_message}
{user_email}
'''
    button = sl.form_submit_button('Submit')
if button:
    send_email(message=message, username=user_email)
    sl.info('Email sent successfully!')