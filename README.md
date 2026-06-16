# Smtp-mailing-client
This is an Email Sender application in Python


Project Description

This is an Email Sender application in Python program that automates the process of sending emails with attachments. It uses the SMTP protocol to connect to an email server, authenticate the sender, compose a message, attach a file, and deliver the email to a specified recipient.

Features
Reads credentials from an external file.
Loads email content from a text file.
Supports file attachments.
Uses MIME formatting for multipart emails.
Sends emails through an SMTP server.
Libraries Used
smtplib — SMTP communication.
email.mime.text — Plain-text message creation.
email.mime.multipart — Multipart email support.
email.mime.base — Attachment handling.
email.encoders — Base64 encoding of attachments.
Workflow
Connect to the SMTP server.
Authenticate the sender.
Create the email message.
Load the message body from a file.
Attach the selected file.
Send the email.
Close the connection.
