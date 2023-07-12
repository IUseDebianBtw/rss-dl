import feedparser
import youtube_dl
import schedule
import time
import os
import logging
from ascii_art import ASCII_ART

# Setup logging
logging.basicConfig(level=logging.INFO)

# pulling from the ascii_art file
logging.info('''

            @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
            @***********@@@@@@@@***********@
            @***********@@@@@@@@***********@
            @***********@@@@@@@@***********@
            @***********@@@@@@@@***********@
            @***********@@@@@@@@***********@
            @***########@@@@@@@@########***@
            @***##@@@@@@@@@@@@@@@@@@@@%#***@
            @******#%@@@@@@@@@@@@@@%#******@
            @*********#%@@@@@@@@%#*********@
            @***********##@@@%#************@
            @**************#***************@
            @******************************@
            @******************************@
            @******************************@
            @%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
                    By: Bossman7309

 ________  ________   ________                 ________  ___          
|\   __  \|\   ____\ |\   ____\               |\   ___ \|\  \         
\ \  \|\  \ \  \___|_\ \  \___|_  ____________\ \  \_|\ \ \  \        
 \ \   _  _\ \_____  \\ \_____  \|\____________\ \  \ \\ \ \  \       
  \ \  \\  \\|____|\  \\|____|\  \|____________|\ \  \_\\ \ \  \____  
   \ \__\\ _\ ____\_\  \ ____\_\  \              \ \_______\ \_______\
    \|__|\|__|\_________\\_________\              \|_______|\|_______|
             \|_________\|_________|                                  

           
'''
)

# Set the RSS feed URL
feed_url = os.getenv('RSS_FEED_URL', 'https://example.com/rss')

logging.info(f'RSS feed URL: {feed_url}')

# Set the download directory directly
download_dir = '/portainer/Files/AppData/Config/rss-dl' 

# Check if directory exists, if not create it and log it
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
    logging.info(f'Download directory did not exist. Created directory: {download_dir}')
else:
    logging.info(f'Download directory exists. No need to create one.')

# logging directory
logging.info(f'Set download directory: {download_dir}')

logging.info('Everything seems to be working')

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


# Schedule the job every 24 hours
schedule.every(24).hours.do(download_videos)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
