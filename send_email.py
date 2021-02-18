import email, smtplib, ssl
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yaml

config_file = "config.yml"
try:
    f = open(config_file, 'r')
except OSError:
    print(f"Could not open/read file: {config_file}")
    
    sys.exit()

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)




subject = cfg['messages']['subject']
body =cfg['messages']['body']
sender_email = cfg['mail']['sender_email']
print(f" Receiver {sys.argv[1]}")
receiver_email = sys.argv[1]
password = cfg['mail']['password']


# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "files/" + sys.argv[2] +".pdf"  # In same directory as script

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
