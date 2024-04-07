# dependencies to send emails
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random    # to generate random 6 digit OTP number


# access the mail of client
with open('data.txt', 'r') as file:
    for i in file:
        data = i.split(",")
        username = data[1]

# Recipient email address
recipient_email = username


# access info of or official account
# use file handelling for security
with open("senddata.txt") as file:
    for i in file:
        data = i.split(",")
        
        # Zoho Mail or Gmail SMTP server details
        smtp_server = data[0]
        smtp_port = data[3] # Zoho Mail or Gmail SMTP port
        
        # Sender's email credentials
        sender_email = data[1]
        password = data[2]


# Create a message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test Email'


# Email body
# create random OTP
random_number = random.randint(100000,999999)
body = f"This is a test email sent from Python using Gmail. Your OTP is {random_number}"  
# create your custome msg above if you want
message.attach(MIMEText(body, 'plain'))


# Now send mail from our official mail account
# Establish a connection with the SMTP server using SSL
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, password)  # Login to the SMTP server
    server.send_message(message)  # Send the email


# Congratulations You just sent email using python i.e step towards streamlining e-mail automation and more !!!