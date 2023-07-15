import os
import requests
import logging
import schedule
import time
import feedparser
import yt_dlp as youtube_dl
from directory_setup import setup_directory
from video_downloader import download_videos
from datetime import datetime, timedelta, timezone

# Initialize logging configuration
def initialize_logging():
    """Initializes a basic logging setup with level set to INFO."""
    logging.basicConfig(level=logging.INFO)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('ascii_art.txt', 'r') as f:
        ascii_art = f.read()
        logging.info(ascii_art)

# Initialize the channel URLs
def initialize_channel_urls():
    """Reads CHANNEL_URLS from environment variables and logs them."""
    channel_urls = os.getenv('CHANNEL_URLS', 'https://www.youtube.com/@MentalOutlaw').split(',')
    for url in channel_urls:
        logging.info(f'Channel URL: {url}')
    return channel_urls

# Get the channel ID
def get_browse_id(channel_url):
    """Retrieves the browse ID for the YouTube channel."""
    response = requests.get(channel_url)
    browse_id = response.text.split('"browseId":"')[1].split('"')[0]
    logging.info(f'Channel ID: {browse_id}')
    return browse_id

# Set the feed URLs
def set_feed_urls(browse_ids):
    """Generates the feed URLs using the browse IDs."""
    feed_urls = [f"https://www.youtube.com/feeds/videos.xml?channel_id={id}" for id in browse_ids]
    for url in feed_urls:
        logging.info(f'Feed URL: {url}')
    return feed_urls

# Initialize the download directory
def initialize_download_dir():
    """Creates the download directory if not exists and logs it."""
    download_dir = '/home/dh/Videos'  # Set the download directory manually
    setup_directory(download_dir)
    logging.info(f'Set download directory: {download_dir}')
    return download_dir

# Initialize video downloads
def initialize_video_downloads(feed_urls, download_dir):
    """Downloads the videos and sets up the schedule for subsequent downloads."""
    for feed_url in feed_urls:
        logging.info(f'Initiating video download for feed {feed_url}')
        download_videos(feed_url, download_dir, datetime.now(timezone.utc) - timedelta(days=1))
        logging.info('Everything seems to be working')

        # Schedule the job every 24 hours
        schedule.every(24).hours.do(download_videos, feed_url, download_dir, datetime.now() - timedelta(days=1))

        # Uncomment below lines for testing purposes
        # schedule.every(1).minutes.do(download_videos, feed_url, download_dir, datetime.now() - timedelta(days=1)) 
        # schedule.every(30).seconds.do(download_videos, feed_url, download_dir, datetime.now() - timedelta(days=1))

    # Start the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    initialize_logging()
    links = initialize_channel_urls()
    feed_urls = []
    for link in links:
        if "youtube.com" in link:
            channel_url = link
            browse_id = get_browse_id(channel_url)
            feed_urls.extend(set_feed_urls([browse_id]))
        else:
            feed_urls.append(link)

    download_dir = initialize_download_dir()
    initialize_video_downloads(feed_urls, download_dir)