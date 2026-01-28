import os
from resend import Resend

# Initialize Resend client
resend = Resend(api_key=os.getenv("RESEND_KEY"))

def send_mail(to, subject, message):
    """
    Send an email using Resend

    Args:
        to (str | list[str]): Recipient email address(es)
        subject (str): Email subject
        message (str): HTML content of the email

    Returns:
        dict: Response with success status and data/error
    """
    try:
        resend_mail = os.getenv("RESEND_MAIL")
        if not resend_mail or not os.getenv("RESEND_KEY"):
            raise ValueError("Missing RESEND_KEY or RESEND_MAIL in environment variables")

        # Ensure `to` is a list for multiple recipients
        if isinstance(to, str):
            to = [to]

        response = resend.emails.send(
            from_email=resend_mail,
            to=to,
            subject=subject,
            html=message
        )
        return {"success": True, "data": response}

    except Exception as e:
        print("Email send error:", e)
        return {"success": False, "error": str(e)}

# Example usage
# send_mail("test@example.com", "Hello", "<h1>This is a test</h1>")
