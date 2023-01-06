import smtplib
import ssl

host = "smtp.gmail.com"
port = "465"

username = "ruthvick2005@gmail.com"
password = "frboooihbacuknbo"

reciever = "ruthvick2005@gmail.com"
message = """
Subject: It works?
Test python email
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, message)