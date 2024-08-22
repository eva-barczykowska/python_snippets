# Necessary imports
import smtplib
from email.message import EmailMessage

# Email settings
sender_email = "eva.barczykowska@gmail.com"
receiver_email = "ewa.barczykowska@t-mobile.cz"
subject = "Email from python"
body = "This is a test email sent using Python."

# Create the email message
message = EmailMessage()
message.set_content(body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

# Connect to the SMTP server and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, "uhbn yuft dnyw ptes")
    smtp.send_message(message)

print("Email sent successfully!")






# Can you explain the purpose of the 'smtplib.SMTP_SSL' function in the code?
# The `smtplib.SMTP_SSL` function in the provided code is used to establish a secure connection to an SMTP
# (Simple Mail Transfer Protocol) server. In this case, it is used to connect to Gmail's SMTP server (`smtp.gmail.com`)
# using SSL (Secure Sockets Layer) encryption.
#
# The `SMTP_SSL` function takes two arguments: the server address and the port number.
# In this case, the server address is `'smtp.gmail.com'` and the port number is `465`.
#
# The `with` statement is used to create a context manager for the SMTP connection.
# This ensures that the connection is properly closed after the email is sent,
# even if an error occurs during the sending process.
#
# Inside the `with` statement, the `login()` method is used to authenticate with the SMTP server using
# the sender's emailaddress and password.
#
# Finally, the `send_message()` method is used to send the email message using the established SMTP connection.

# In summary, the `smtplib.SMTP_SSL` function is used to establish a secure connection to an SMTP server, and the `with`
# statement is used to create a context manager for the SMTP connection. The `login()` method is used to authenticate
# with the SMTP server, and the `send_message()` method is used to send the email message.
