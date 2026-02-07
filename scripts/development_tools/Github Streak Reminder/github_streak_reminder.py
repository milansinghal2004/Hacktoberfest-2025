import os
import requests
import argparse
from datetime import datetime, timezone
from plyer import notification
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def check_github_activity(username, token=None):
    """
    Checks if the user has any activity (PushEvent, CreateEvent, PullRequestEvent) today.
    """
    url = f"https://api.github.com/users/{username}/events"
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        events = response.json()
        
        today = datetime.now(timezone.utc).date()
        
        for event in events:
            event_date = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).date()
            if event_date == today:
                # Interesting events that count towards a streak
                if event["type"] in ["PushEvent", "CreateEvent", "PullRequestEvent", "IssuesEvent"]:
                    return True
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub activity: {e}")
        return None

def send_notification():
    """
    Sends a Windows toast notification.
    """
    notification.notify(
        title="GitHub Streak Alert! 🔔",
        message="You haven't made any commits today. Don't let your streak break!",
        app_name="GitHub Streak Reminder",
        timeout=10
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub Streak Reminder")
    parser.add_argument("--test", action="store_true", help="Force a notification for testing")
    args = parser.parse_args()

    if args.test:
        print("Test mode enabled: Sending forced notification...")
        send_notification()
    elif not GITHUB_USERNAME:
        print("Please set GITHUB_USERNAME in your .env file.")
    else:
        activity_found = check_github_activity(GITHUB_USERNAME, GITHUB_TOKEN)
        
        if activity_found is False:
            print("No activity found today. Sending notification...")
            send_notification()
        elif activity_found is True:
            print("Activity found today! Streak is safe.")
        else:
            print("Could not determine activity status due to errors.")
