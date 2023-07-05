import feedparser
import youtube_dl
import schedule
import time

def download_videos():
    # specify the RSS feed url
    feed_url = "https://rss.art19.com/part-of-the-problem"

    # parse the feed
    feed = feedparser.parse(feed_url)

    # setup youtube_dl options
    ydl_opts = {
        'outtmpl': '/home/bossman7309/Videos',
    }

    # for each entry in the feed
    for entry in feed.entries:
        # for each link in the entry
        for link in entry.links:
            # if the link is a video
            if "video" in link.type:
                # download the video using youtube_dl
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link.href])

# schedule the job every 24 hours
schedule.every(24).hours.do(download_videos)

# keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
