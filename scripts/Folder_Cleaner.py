import os
import time

def clean_old_files(folder_path, days=30):
    """
    Deletes files in the specified folder that are older than the given number of days.

    Args:
        folder_path (str): Path to the folder to clean.
        days (int, optional): Number of days to retain files. Files older than
            this threshold will be deleted. Defaults to 30.

    Returns:
        None

    Example:
        >>> clean_old_files("C:/Users/Sahithi/Downloads", days=7)
        Deleted: old_report.txt
        Deleted: temp.zip
    """

    # Verify that the folder exists before proceeding
    if not os.path.exists(folder_path):
        print("❌ The specified folder does not exist.")
        return

    # Get the current time
    now = time.time()
    deleted_files = 0

    # Iterate through all files in the folder
    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        # Process only files (ignore subfolders)
        if os.path.isfile(path):
            # Check if file modification time is older than the threshold
            if os.stat(path).st_mtime < now - days * 86400:
                os.remove(path)
                deleted_files += 1
                print(f"🗑️ Deleted: {file}")

    print(f"✅ Cleaned {deleted_files} old files older than {days} days.")


if __name__ == "__main__":
    # Ask user for folder path and days threshold
    folder = input("Enter the folder path to clean: ").strip()
    try:
        days = int(input("Delete files older than how many days? (default 30): ") or 30)
    except ValueError:
        days = 30
    clean_old_files(folder, days)
