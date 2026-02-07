# GitHub Streak Reminder Setup Guide

This tool monitors your GitHub activity and sends a Windows notification if you haven't made a commit today.

## ⚙️ Configuration

1.  **Create a `.env` file**: 
    Rename `.env.template` to `.env` in this directory.
2.  **Fill in your details**:
    - `GITHUB_USERNAME`: Your GitHub username.
    - `GITHUB_TOKEN`: (Optional) A Personal Access Token. Recommended for private repo tracking and higher rate limits.

## 🚀 How to Run

```bash
python github_streak_reminder.py
```

- If activity is found, it will log: `Activity found today! Streak is safe.`
- If no activity is found, a Windows Toast Notification will appear.

## ⏰ Automation (Windows Task Scheduler)

To make this check automatic every night:

1.  Open **Task Scheduler** on your computer.
2.  Click **Create Basic Task**.
3.  Name it `GitHub Streak Reminder`.
4.  **Trigger**: Set it to **Daily** at a time you usually want the reminder (e.g., 8:00 PM).
5.  **Action**: Select **Start a Program**.
    - **Program/script**: Path to your `python.exe`.
    - *How to find it:* Open terminal and type `where python`. Copy the full path that ends in `python.exe`.
    - **Add arguments**: The absolute path to the script, e.g., `E:\PYTHON\Hacktoberfest 2k25\Hacktoberfest-2025\scripts\development_tools\github_streak_reminder.py`
    - **Start in**: The directory where the script is located (so it can find `.env`), e.g., `E:\PYTHON\Hacktoberfest 2k25\Hacktoberfest-2025\scripts\development_tools\`
6.  Click **Finish**.

Now, you'll get a nudge every night if you forget to commit!
