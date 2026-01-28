from pytube import YouTube
import os
from datetime import datetime

def download_video(url, path="."):
    """Downloads a YouTube video in highest resolution with progress feedback."""

    try:
        yt = YouTube(url)
        print(f"🎥 Title: {yt.title}")
        print("📡 Fetching stream information...")

        stream = yt.streams.get_highest_resolution()
        filename = stream.default_filename
        output_path = os.path.join(path, filename)

        # Download video
        print("⬇️ Downloading...")
        stream.download(output_path=path)
        print(f"✅ Download complete: {output_path}")

        # Log download
        log_file = os.path.join(path, "download_log.txt")
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {yt.title} ({url})\n")
        print(f"📝 Log updated: {log_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    save_path = input("Enter destination folder (leave empty for current): ").strip() or "."
    download_video(video_url, save_path)
