import os
import requests

def send_mail(to, subject, message):
    """
    Send an email using Brevo (via REST API)

    Args:
        to (str | list[str]): Recipient email address(es)
        subject (str): Email subject
        message (str): HTML content of the email

    Returns:
        dict: Response with success status and data/error
    """
    try:
        brevo_key = os.getenv("BREVO_KEY")
        brevo_mail = os.getenv("BREVO_MAIL")

        if not brevo_key or not brevo_mail:
            raise ValueError("Missing BREVO_KEY or BREVO_MAIL in environment variables")

        # Prepare payload
        recipients = [{"email": email} for email in to] if isinstance(to, list) else [{"email": to}]
        payload = {
            "sender": {"email": brevo_mail},
            "to": recipients,
            "subject": subject,
            "htmlContent": message
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": brevo_key
        }

        # Send request
        res = requests.post("https://api.brevo.com/v3/smtp/email", json=payload, headers=headers)
        data = res.json()

        if not res.ok:
            raise ValueError(data.get("message", "Brevo API error"))

        return {"success": True, "data": data}

    except Exception as e:
        print("Email send error:", e)
        return {"success": False, "error": str(e)}

# Example usage
# send_mail("test@example.com", "Hello", "<h1>This is a test</h1>")
