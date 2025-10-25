import os
import shutil
from datetime import datetime

def organize_files(folder_path, log_activity=True):
    """Organizes files into subfolders by their extension and logs the actions."""

    if not os.path.exists(folder_path):
        print("❌ The specified folder does not exist.")
        return

    moved_files = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if not os.path.isfile(file_path):
            continue

        ext = os.path.splitext(filename)[1].lower().replace('.', '') or "no_extension"
        folder = os.path.join(folder_path, ext)
        os.makedirs(folder, exist_ok=True)
        new_path = os.path.join(folder, filename)
        shutil.move(file_path, new_path)
        moved_files.append((filename, new_path))

    print(f"✅ Organized {len(moved_files)} files by extension.")

    # Optional logging
    if log_activity and moved_files:
        log_file = os.path.join(folder_path, "organizer_log.txt")
        with open(log_file, "a") as log:
            log.write(f"\nRun on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            for old, new in moved_files:
                log.write(f"Moved: {old} -> {new}\n")
        print(f"📝 Log saved to {log_file}")


if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
