import imaplib  # For accessing emails via IMAP
import email    # For parsing email messages
from email.header import decode_header
import re       #To create OTP pattern

# now fetch the login details from CSV file one by one

with open('data.txt', 'r') as file:
    for i in file:
        data = i.split(",")
        imap_server = data[0]
        username = data[1]
        password = data[2]


mail = imaplib.IMAP4_SSL(imap_server)


mail.login(username, password)


mail.select("INBOX")


# search_criteria = '(FROM "sender@example.com")'
# result, data = mail.search(None, search_criteria)

result, data = mail.search(None, "ALL")


email_ids = data[0].split()

otps = []

for mail_id in email_ids:
    # Fetch the email using its ID
    result, raw_email = mail.fetch(mail_id, "(RFC822)")
    
    # Parse the email data
    email_message = email.message_from_bytes(raw_email[0][1])
    
    # Extract email details
    subject = email_message["Subject"]
    sender = email.utils.parseaddr(email_message["From"])[1]
    
    # Print email details
    
    # print("Subject:", subject)
    # print("Sender:", sender)
    
    body = ""
    
    
    # Get email body if exists
    if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
    else:
            body = email_message.get_payload(decode=True).decode()
            
            
    # Check if OTP exists in the email body
    otp_match = re.search(r'\b\d{6}\b|\b\d{3}\s\d{3}\b', body)
    if otp_match:
            otp = otp_match.group()
            otps.append(otp)


if otps:
    print("Found OTPs:", otps[-1])
else:
    print("No OTPs found")
  

mail.logout()