import os
import requests
import logging
import schedule
import time
import feedparser
import yt_dlp as youtube_dl
from directory_setup import setup_directory
from video_downloader import download_videos

# Initialize logging configuration
def initialize_logging():
    """Initializes a basic logging setup with level set to INFO."""
    logging.basicConfig(level=logging.INFO)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('ascii_art.txt', 'r') as f:
        ascii_art = f.read()
        logging.info(ascii_art)

# Initialize the channel URL
def initialize_channel_url():
    """Reads CHANNEL_URL from environment variables and logs it."""
    channel_url = os.getenv('CHANNEL_URL', 'https://www.youtube.com/@Fireship')
    logging.info(f'Channel URL: {channel_url}')
    return channel_url

# Get the channel ID
def get_browse_id(channel_url):
    """Retrieves the browse ID for the YouTube channel."""
    response = requests.get(channel_url)
    browse_id = response.text.split('"browseId":"')[1].split('"')[0]
    logging.info(f'Channel ID: {browse_id}')
    return browse_id

# Set the feed URL
def set_feed_url(browse_id):
    """Generates the feed URL using the browse ID."""
    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={browse_id}"
    logging.info(f'Feed URL: {feed_url}')
    return feed_url

# Initialize the download directory
#def initialize_download_dir():
#    """Reads DOWNLOAD_DIR from environment variables, creates it if not exists, and logs it."""
#    download_dir = os.getenv('DOWNLOAD_DIR')
#    setup_directory(download_dir)
#    logging.info(f'Set download directory: {download_dir}') #
#    return download_dir


def initialize_download_dir():
    """Creates the download directory if not exists and logs it."""
    download_dir = '/media/bossman7309/Bossmanhhd'  # Set the download directory manually (for testing purposes only)
    setup_directory(download_dir)
    logging.info(f'Set download directory: {download_dir}')
    return download_dir


# Download videos
def initialize_video_downloads(feed_url, download_dir):
    """Downloads the videos and sets up the schedule for subsequent downloads."""
    logging.info('Initiating video download')

    # Parse the feed
    feed = feedparser.parse(feed_url)


    # Get the current time and subtract 24 hours to get the time 24 hours ago
    time_24_hours_ago = time.mktime(time.gmtime()) - 24*60*60

    # A flag to indicate if any new videos were found
    new_videos_found = False

    # For each entry in the feed
    for entry in feed.entries:
        # For each link in the entry
        for link in entry.links:
            # If the link is a video
            if 'youtube.com/watch?v=' in link.href:
                # Check if the video was published within the last 24 hours
                if time.mktime(entry.published_parsed) > time_24_hours_ago:
                    # Download the video
                    download_videos(link.href, download_dir)
                    new_videos_found = True
            else:
                # If the link is not a YouTube video, download it regardless of publication time
                download_videos(link.href, download_dir)
                new_videos_found = True

    if not new_videos_found:
        logging.info("No new videos found in the last 24 hours. Stopping script.")
        exit(0)  # Exit the script if no new videos were found
            # Schedule the job every 24 hours

    schedule.every(24).hours.do(initialize_video_downloads, feed_url, download_dir)

    while True:
        schedule.run_pending()
        time.sleep(1)


        
if __name__ == "__main__":
    initialize_logging()
    link = initialize_channel_url()
    if "youtube.com" in link:
        channel_url = link
        browse_id = get_browse_id(channel_url)
        feed_url = set_feed_url(browse_id)
        download_dir = initialize_download_dir()
        initialize_video_downloads(feed_url, download_dir)
    else:
        feed_url = link
        download_dir = initialize_download_dir()
        initialize_video_downloads(feed_url, download_dir)