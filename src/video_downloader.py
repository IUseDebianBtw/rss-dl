import feedparser
import yt_dlp as youtube_dl
import os
import logging
import requests

def download_videos(youtube_url, download_dir):
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }   #'quiet': True,

    # Download the video using youtube_dl
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        logging.info(f'Successfully downloaded video: {youtube_url}')
    except PermissionError:
        logging.error(f'Permission denied when trying to download video: {youtube_url}')
    except Exception as e:
        logging.error(f'Failed to download video: {youtube_url} - {str(e)}')

def download_videos_from_feed(feed_url, download_dir):
    # Parse the feed
    feed = feedparser.parse(feed_url)
    line_separated_json = '\n'.join(str(feed).split(','))
    logging.info(f'Feed: {line_separated_json}')
    

    # For each entry in the feed
    for entry in feed.entries:
        # For each link in the entry
        for link in entry.links:
            # If the link is a video
            if 'youtube.com/watch?v=' in link.href:
                # Download the video
                download_videos(link.href, download_dir)