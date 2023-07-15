import feedparser
import yt_dlp as youtube_dl
import os
import logging
import requests
from datetime import datetime

def download_videos(youtube_url, download_dir, time_limit):
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }

    # Parse the feed
    feed = feedparser.parse(youtube_url)

    # For each entry in the feed
    for entry in feed.entries:
        # For each link in the entry
        for link in entry.links:
            # If the link is a video
            if 'youtube.com/watch?v=' in link.href:
                # Parse the published time into a datetime object
                published_time = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%S%z")
                # If the video was published within the last 24 hours
                if published_time > time_limit:
                    # Download the video using youtube_dl
                    try:
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([link.href])
                        logging.info(f'Successfully downloaded video: {link.href}')
                    except PermissionError:
                        logging.error(f'Permission denied when trying to download video: {link.href}')
                    except Exception as e:
                        logging.error(f'Failed to download video: {link.href} - {str(e)}')