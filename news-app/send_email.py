import smtplib, ssl #creates a secure connection to an email server
from email.mime.text import MIMEText #std for formatting emails - simple text emails
from email.mime.multipart import MIMEMultipart # for complex emails say attachments etc
from dotenv import load_dotenv
import os
load_dotenv()

def send_email(subject, body, to_email):
    host = "smtp.gmail.com"
    port = 587
    from_email = "aishuk3@gmail.com"
    password = os.getenv("GMAIL_APP_PASSWORD")

 # Create proper email structure
    msg = MIMEMultipart() #msg is like an envelope
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain')) #add body from main file

    try:
        #connect to Gmail's smtp server
        server= smtplib.SMTP(host, port) 
        server.starttls() #secure the connection - TLS
        server.login(from_email, password)
        #send email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit() #close connection
        print("✅ Email sent successfully!")
    
    except Exception as e:

        print(f"❌ Error sending email: {e}")
