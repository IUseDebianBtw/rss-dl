import feedparser
import youtube_dl
from datetime import datetime, timedelta
import os
import logging

def download_videos(feed_url, download_dir):
    logging.info('Starting video download job...')

    # Parse the feed
    try:
        feed = feedparser.parse(feed_url)
    except Exception as e:
        logging.error(f'Failed to parse feed: {feed_url} - {str(e)}')
        return

    # Setup youtube_dl options
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }

    # Get the current time (now) and 24 hours ago (one_day_ago)
    now = datetime.now()
    one_day_ago = now - timedelta(days=1)

    # For each entry in the feed
    for entry in feed.entries:
        # Get the published time of the entry
        published_time = datetime(*entry.published_parsed[:6])

        # If the entry was published in the last 24 hours
        if one_day_ago <= published_time <= now:
            # For each link in the entry
            for link in entry.links:
                # If the link is a video
                if "video" in link.type:
                    # Download the video using youtube_dl
                    try:
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([link.href])
                        logging.info(f'Successfully downloaded video: {link.href}')
                    except PermissionError:
                        logging.error(f'Permission denied when trying to download video: {link.href}')
                    except Exception as e:
                        logging.error(f'Failed to download video: {link.href} - {str(e)}')
