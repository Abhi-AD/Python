import yt_dlp

link = input("Enter link to :")

ydl_opts = {"format": "best", "outtmpl": "%(title)s.%(ext)s"}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Download Successful!")
