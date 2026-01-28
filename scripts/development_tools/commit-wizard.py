import subprocess
from datetime import datetime

#this function checks if git is initialized
def check_git_repo():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout.strip() == "true":
            print("You are inside a Git repository.")
            return True
    except subprocess.CalledProcessError:
        print("Not in a Git repository.")
        return False

#checks if it has changes
def has_changes():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )
    return bool(result.stdout.strip())

def get_commit_message():
    user_input = input("Enter commit message (press Enter for default): ")
    if user_input.strip() == "":
        return f"Auto commit {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    return user_input

def stage_commit_push(commit_message):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Changes pushed successfully!")
    except subprocess.CalledProcessError:
        print("⚠️ No changes to commit or push, or an error occurred.")

def main():
    if not check_git_repo():
        print("❌ Not a Git repository. Please run inside a Git repo.")
        return

    if not has_changes():
        print("⚠️ No changes to commit or push.")
        return

    msg = get_commit_message()
    stage_commit_push(msg)

if __name__ == "__main__":
    main()

