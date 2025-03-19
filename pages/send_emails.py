import smtplib,ssl

host = 'smtp.gmail.com'
port = 465

username = 'josephchimaobi099@gmail.com'
password = 'lquj ogep jyzb timy'
receiver= 'josephvianney903@gmail.com'
message = '''\
Subject: Hello,
how was your experience on the first 
two days on our app,
we would love to work with you

'''
context_source = ssl.create_default_context()
with smtplib.SMTP_SSL(host=host,context=context_source,port=port) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)