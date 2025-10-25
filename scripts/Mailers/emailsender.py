import smtplib
from email.mime.text import MIMEText

def send_email(sender, password, receiver, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("✅ Email sent successfully!")

if __name__ == "__main__":
    send_email("your_email@gmail.com", "your_password",
               "receiver_email@gmail.com", "Test Mail", "Hello from Python!")
