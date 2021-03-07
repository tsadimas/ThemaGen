import email, smtplib, ssl
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import themagen.log
import themagen.config
import themagen.users


_logger = themagen.log.get(__name__)  

def submit():
    try:
        cfg = themagen.config.read()
        users = themagen.users.read_csv()
        for user in users:
           _email(user, cfg)
    except:
        _logger.error('program exit with error')
        sys.exit(1)


def _email(user: themagen.users.User, cfg):
    subject = cfg['messages']['subject']
    body =cfg['messages']['body']
    sender_email = cfg['mail']['sender_email']
    print(f" Receiver {user.email}")
    receiver_email = user.email
    password = cfg['mail']['password']

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "assets/files/" + user.full_name_sanitized +".pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()

    with smtplib.SMTP(cfg['mail']['host'], cfg['mail']['port']) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
