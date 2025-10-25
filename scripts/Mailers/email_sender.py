import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import datetime

# ------------------ User Inputs ------------------
sender_email = input("Enter your email: ")
password = input("Enter your password or app-specific password: ")

# Multiple recipients (comma-separated)
to_emails = input("Enter recipient emails (comma-separated): ").split(",")
cc_emails = input("Enter CC emails (comma-separated, leave blank if none): ").split(",") if input("Add CC? (y/n): ").lower()=="y" else []
bcc_emails = input("Enter BCC emails (comma-separated, leave blank if none): ").split(",") if input("Add BCC? (y/n): ").lower()=="y" else []

subject = input("Enter email subject: ")
body_type = input("Email type? Plain(1) / HTML(2): ")

if body_type=="2":
    body = input("Enter HTML body: ")
else:
    body = input("Enter plain text body: ")

# Multiple attachments
attachments = []
while True:
    file_path = input("Enter path to attachment (leave blank to stop adding): ")
    if not file_path:
        break
    attachments.append(file_path)

# ------------------ Compose Email ------------------
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ", ".join(to_emails)
msg['CC'] = ", ".join(cc_emails)
msg['Subject'] = subject

# Attach body
if body_type=="2":
    msg.attach(MIMEText(body, 'html'))
else:
    msg.attach(MIMEText(body, 'plain'))

# Attach files
for f in attachments:
    try:
        with open(f, "rb") as file:
            part = MIMEApplication(file.read(), Name=os.path.basename(f))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(f)}"'
        msg.attach(part)
        print(f"Attachment added: {f}")
    except Exception as e:
        print(f"Failed to attach {f}: {e}")

# ------------------ Send Email ------------------
all_recipients = to_emails + cc_emails + bcc_emails
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    
    for recipient in all_recipients:
        try:
            server.sendmail(sender_email, recipient.strip(), msg.as_string())
            print(f"✅ Email sent to {recipient}")
        except Exception as e:
            print(f"❌ Failed to send email to {recipient}: {e}")
    
    server.quit()
except Exception as e:
    print(f"❌ SMTP connection failed: {e}")

# ------------------ Logging ------------------
log_file = "email_log.txt"
with open(log_file, "a") as log:
    log.write(f"{datetime.datetime.now()} - Subject: {subject} - Sent to: {all_recipients}\n")
print(f"Log saved to {log_file}")
