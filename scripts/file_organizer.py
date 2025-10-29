import os
import shutil
from datetime import datetime

def organize_files(folder_path, log_activity=True):
    """
    Organizes files in the specified folder into subfolders based on file extension.

    Each file is moved into a subfolder named after its extension
    (e.g., '.txt' → 'txt' folder). Files without an extension are moved
    to a folder named 'no_extension'.

    Optionally logs all file movements to 'organizer_log.txt' in the main directory.

    Args:
        folder_path (str): Path to the folder containing files to organize.
        log_activity (bool, optional): Whether to record actions in a log file.
            Defaults to True.

    Returns:
        None

    Example:
        >>> organize_files("C:/Users/Sahithi/Downloads")
        ✅ Organized 15 files by extension.
        📝 Log saved to C:/Users/Sahithi/Downloads/organizer_log.txt
    """

    # Ensure the given folder path exists
    if not os.path.exists(folder_path):
        print("❌ The specified folder does not exist.")
        return

    moved_files = []

    # Iterate through all files in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip subfolders and process only files
        if not os.path.isfile(file_path):
            continue

        # Extract file extension; handle files without extensions
        ext = os.path.splitext(filename)[1].lower().replace('.', '') or "no_extension"
        folder = os.path.join(folder_path, ext)

        # Create the extension folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # Move the file to its new destination
        new_path = os.path.join(folder, filename)
        shutil.move(file_path, new_path)
        moved_files.append((filename, new_path))

    print(f"✅ Organized {len(moved_files)} files by extension.")

    # Log activity if enabled and any files were moved
    if log_activity and moved_files:
        log_file = os.path.join(folder_path, "organizer_log.txt")
        with open(log_file, "a") as log:
            log.write(f"\nRun on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            for old, new in moved_files:
                log.write(f"Moved: {old} -> {new}\n")
        print(f"📝 Log saved to {log_file}")


if __name__ == "__main__":
    # Prompt user to input folder path and execute the organizer
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
