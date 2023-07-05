import feedparser
import youtube_dl
import schedule
import time
import os

# Retrieve the RSS feed URL and download directory from the environment variables
feed_url = os.environ.get('RSS_FEED_URL', 'https://example.com/rss')
download_dir = os.environ.get('DOWNLOAD_DIR', '/portainer/Files/AppData/Config/rssDownloader')

def download_videos():
    # Parse the feed
    feed = feedparser.parse(feed_url)

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
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link.href])

# Schedule the job every 24 hours
schedule.every(24).hours.do(download_videos)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
