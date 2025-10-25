```
# 📨 Mailers

This directory contains utility scripts for sending emails using two providers: **Resend** and **Brevo**.

## 📦 Providers

### Resend
- A developer-friendly email API.
- Requires `RESEND_API_KEY` and `SENDER_EMAIL` environment variables.
- Usage example:
```javascript
import { sendWithResend } from './resendMailer';

sendWithResend('recipient@example.com', 'Subject', '<p>Email body</p>');
```

### Brevo
- Email marketing and transactional email service (formerly Sendinblue).
- Requires `BREVO_API_KEY` and `SENDER_EMAIL` environment variables.
- Usage example:
```javascript
import { sendWithBrevo } from './brevoMailer';

sendWithBrevo('recipient@example.com', 'Subject', '<p>Email body</p>');
```

## ⚙️ Setup
Set the following environment variables in your project:
- `RESEND_API_KEY`
- `BREVO_API_KEY`
- `SENDER_EMAIL`
