import feedparser
import youtube_dl
import schedule
import time
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Set the RSS feed URL
feed_url = os.environ.get('RSS_FEED_URL', 'https://example.com/rss')

# Set the download directory directly
download_dir = '/media/bossman7309/ORANGEHHD1/uploads'  # Change this to your desired pat /portainer/Files/AppData/Config/rssDownloader

# Log the directory
logging.info(f'Set download directory: {download_dir}')

logging.info('everything seems to be working')

def download_videos():
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

    # For each entry in the feed
    for entry in feed.entries:
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

    logging.info('Video download job completed.')

# Schedule the job every 24 hours
schedule.every(24).hours.do(download_videos)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
