# Email Sender with Attachment

## Overview

This Python application automates the process of sending emails with file attachments using the SMTP protocol.

The program:

* Connects to an SMTP server.
* Authenticates the sender using credentials stored in a separate file.
* Loads the email content from a text file.
* Attaches a specified file.
* Sends the email to the recipient.

This project was developed as a practical exercise to learn Python networking, file handling, and email automation.

---

## Features

* Send plain-text emails.
* Attach files of any type.
* Store passwords outside the source code.
* Modular configuration through variables.
* Uses secure TLS communication.

---

## Requirements

* Python 3.8 or newer
* Internet connection
* A valid email account with SMTP access

### Python Libraries

The script only uses Python standard libraries:

* smtplib
* email.mime.text
* email.mime.base
* email.mime.multipart
* email.encoders

No external packages are required.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/email-sender.git
cd email-sender
```

### 2. Create the password file

Create a file named:

```text
password.txt
```

and place your email password (or App Password) inside it.

Example:

```text
your_app_password_here
```

### 3. Create the message file

Create:

```text
message.txt
```

Example:

```text
Hello,

This email was sent automatically using Python.

Best regards.
```

### 4. Add an attachment

Place any file you want to send inside the project folder.

Example:

```text
image.webp
```

### 5. Configure the script

Edit the configuration section:

```python
SENDER_EMAIL = "your_email@gmail.com"
RECIPIENT_EMAIL = "recipient@example.com"
EMAIL_SUBJECT = "Test Email"
ATTACHMENT_FILE = "image.webp"
```

---

## Usage

Run the script:

```bash
python main.py
```

If the email is successfully sent, the terminal will display:

```text
Email sent successfully.
```

---

## Testing

### Test 1: Basic Email

1. Remove the attachment section.
2. Send a simple email.
3. Verify that the recipient receives the message.

### Test 2: Attachment Delivery

1. Add a small file.
2. Send the email.
3. Verify that the attachment arrives correctly.

### Test 3: Authentication Failure

1. Enter an incorrect password.
2. Run the script.
3. Verify that the SMTP server rejects the login.

### Test 4: Missing File

1. Delete or rename the attachment.
2. Run the script.
3. Verify that Python raises a file-related exception.

---

## Security Notes

* Never hardcode passwords into the source code.
* Never upload password.txt to GitHub.
* Add password.txt to .gitignore.
* Prefer App Passwords over account passwords when supported.

---

## Future Improvements

* Graphical user interface (GUI)
* Multiple recipients
* HTML email support
* Better exception handling
* Configuration through a JSON file
* Logging system
