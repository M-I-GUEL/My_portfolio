import smtplib,ssl
def send_email(message, username):
    host = 'smtp.gmail.com'
    port = 465
    password = 'lquj ogep jyzb timy'
    receiver = 'josephvianney903@gmail.com'

    context_source = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=host,context=context_source,port=port) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)