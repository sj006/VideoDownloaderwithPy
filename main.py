import os
import pandas as pd
from yt_dlp import YoutubeDL

EXCEL_FILE = "Damnit.xlsx"
DOWNLOAD_FOLDER = "downloads"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

df = pd.read_excel(EXCEL_FILE)

def download_video(url, save_path):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': save_path,
        'quiet': False
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded: {save_path}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

for index, row in df.iterrows():
    uni_id = str(row['uni_id'])
    video_link = str(row['Video Link'])
    source = str(row['Source']).strip().lower()

    if video_link == "nan" or video_link.strip() == "":
        print(f"No link for {uni_id}")
        continue

    save_path = os.path.join(DOWNLOAD_FOLDER, f"{uni_id}.mp4")

    # Just download whatever link is provided
    # yt-dlp supports both YouTube and Instagram
    download_video(video_link, save_path)