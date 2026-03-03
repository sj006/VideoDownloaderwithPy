# 🎥 Video Downloader (YouTube + Instagram)

A Python-based bulk video downloader that reads video links from an
Excel file and downloads them automatically.

Each video is saved in the format:

`<uni_id>`{=html}.mp4

Example: 101.mp4\
202.mp4

------------------------------------------------------------------------

## 📌 Features

-   Bulk download using Excel file
-   Supports YouTube videos
-   Supports Instagram public posts
-   Saves files as `<uni_id>.mp4`
-   Automatically creates download folder
-   Clean and simple setup

------------------------------------------------------------------------

## 📂 Project Structure
```
VideoDownloader/ 
│ 
├── main.py
├── Damnit.xlsx 
├── requirements.txt 
├──README.md 
└── downloads/
```

------------------------------------------------------------------------

## 📊 Excel Format Required

Your Excel file (`Damnit.xlsx`) must contain these columns:

  Column Name   Description
  ------------- ----------------------------
  uni_id        Unique ID used as filename
  VideoLink     Full video URL
  Source        Youtube / Instagram

Example:

  uni_id   VideoLink                   Source
  -------- --------------------------- -----------
  101      https://youtube.com/...     Youtube
  102      https://instagram.com/...   Instagram

⚠ Column names are case-sensitive.

------------------------------------------------------------------------

## 🛠 Requirements

-   Python 3.9+
-   Internet connection
-   Public video links

------------------------------------------------------------------------

## 🚀 Setup Instructions

### 1️⃣ Clone or Download Project

If using Git:

git clone `<your-repo-url>`{=html} cd VideoDownloader

------------------------------------------------------------------------

### 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv

Activate it:

Windows (PowerShell): venv`\Scripts`{=tex}`\Activate`{=tex}

Windows (CMD): venv`\Scripts`{=tex}`\activate`{=tex}

------------------------------------------------------------------------

### 3️⃣ Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## 📦 requirements.txt

pandas\
yt-dlp\
openpyxl

------------------------------------------------------------------------

## ▶️ Run The Script

python main.py

All downloaded videos will be saved in:

downloads/`<uni_id>`{=html}.mp4

------------------------------------------------------------------------

## 🔐 Instagram Notes

-   Works for public posts
-   Private accounts may require browser cookies
-   Make sure you are logged into Instagram if needed

------------------------------------------------------------------------

## ⚠ Common Errors

If you get:

KeyError

Check your Excel column names. They must match: - `uni_id` -
`VideoLink` - `Source`

------------------------------------------------------------------------

## ⚙ How It Works

1.  Reads Excel using pandas
2.  Iterates through each row
3.  Extracts `uni_id` and `VideoLink`
4.  Downloads video using yt-dlp
5.  Saves file as `<uni_id>.mp4`

------------------------------------------------------------------------

## 📜 Disclaimer

This project is for educational and personal use only.\
Please respect platform terms of service when downloading content.
