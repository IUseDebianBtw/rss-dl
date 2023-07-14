FROM python:3.8-slim

WORKDIR /app

# Set Environment Variables
ENV RSS_FEED_URL=https://example.com/rss

# Install dependencies
RUN pip install feedparser youtube_dl schedule

# Copy your scripts
COPY main.py ./main.py
COPY ascii_art.py ./ascii_art.py
COPY directory_setup.py ./directory_setup.py 
COPY video_downloader.py ./video_downloader.py 

CMD [ "python", "./main.py" ]
