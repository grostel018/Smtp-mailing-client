"""
Email Sender with Attachment

This program sends an email using SMTP and attaches a file.
The sender credentials are read from a text file and the
message body is loaded from another text file.

Author: Rostel Geni
Date: June 2026
"""
# NOTE:
# The password file must contain a valid email password or app password.
# Replace the placeholder values above with your own email information.


import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# =========================
# Configuration Variables
# =========================

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "your_email@gmail.com"
SENDER_NAME = "Your Name"

RECIPIENT_EMAIL = "recipient_email@example.com"
EMAIL_SUBJECT = "Email Subject"

PASSWORD_FILE = "password.txt"
MESSAGE_FILE = "message.txt"
ATTACHMENT_FILE = "attachment_file.extension"


# =========================
# Read Password
# =========================

with open(PASSWORD_FILE, "r") as f:
    password = f.read().strip()


# =========================
# Connect to SMTP Server
# =========================

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

# Start encrypted connection (TLS)
server.starttls()

# Authenticate sender account
server.login(SENDER_EMAIL, password)


# =========================
# Create Email Message
# =========================

msg = MIMEMultipart()

msg["From"] = SENDER_NAME
msg["To"] = RECIPIENT_EMAIL
msg["Subject"] = EMAIL_SUBJECT


# =========================
# Load Email Body
# =========================

with open(MESSAGE_FILE, "r") as f:
    message = f.read()

# Attach plain-text message to email
msg.attach(MIMEText(message, "plain"))


# =========================
# Attach File
# =========================

with open(ATTACHMENT_FILE, "rb") as attachment:
    file_part = MIMEBase("application", "octet-stream")
    file_part.set_payload(attachment.read())

# Encode attachment in Base64
encoders.encode_base64(file_part)

# Add attachment header
file_part.add_header(
    "Content-Disposition",
    f"attachment; filename={ATTACHMENT_FILE}"
)

# Attach file to email
msg.attach(file_part)


# =========================
# Send Email
# =========================

text = msg.as_string()

server.sendmail(
    SENDER_EMAIL,
    RECIPIENT_EMAIL,
    text
)

# Close SMTP connection
server.quit()

print("Email sent successfully.")
