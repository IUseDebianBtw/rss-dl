import feedparser
import youtube_dl
import schedule
import time
import os
import logging
from ascii_art import ASCII_ART
from directory_setup import setup_directory
from video_downloader import download_video

# Setup logging
logging.basicConfig(level=logging.INFO)

# pulling from the ascii_art file
logging.info(ASCII_ART)

# Set the RSS feed URL  # https://example.com/rss
feed_url = os.getenv('RSS_FEED_URL', 'https://www.youtube.com/@BrodieRobertson')

logging.info(f'RSS feed URL: {feed_url}')

# Set the download directory directly
download_dir = '/home/bossman7309/Videos' 

# Check if directory exists, if not create it and log it
setup_directory(download_dir)

# logging directory
logging.info(f'Set download directory: {download_dir}')

logging.info('Everything seems to be working')

download_video(feed_url, download_dir)


# Schedule the job every 24 hours
#schedule.every(24).hours.do(download_videos)
# schedule.every(1).minutes.do(download_videos)       # testing purposes only
# schedule.every(30).seconds.do(download_videos)

# schedule.every(5).seconds.do(download_videos)

schedule.every(5).seconds.do(download_video, feed_url, download_dir)
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
