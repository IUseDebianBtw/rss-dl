import feedparser
import youtube_dl
from datetime import datetime, timedelta
import os
import logging

def download_video(youtube_url, download_dir):
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }

    # Download the video using youtube_dl
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        logging.info(f'Successfully downloaded video: {youtube_url}')
    except PermissionError:
        logging.error(f'Permission denied when trying to download video: {youtube_url}')
    except Exception as e:
        logging.error(f'Failed to download video: {youtube_url} - {str(e)}')

def test_download_video(download_dir, youtube_urls):
    for url in youtube_urls:
        download_video(url, download_dir)

if __name__ == "__main__":
    test_download_video('/home/bossman7309/Videos', ['https://www.youtube.com/watch?v=AjXLblBzWvs']) 
