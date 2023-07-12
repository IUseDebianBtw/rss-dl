FROM python:3.8-slim

WORKDIR /app

# Set Environment Variables
ENV RSS_FEED_URL=https://example.com/rss

# Install dependencies
RUN pip install feedparser youtube_dl schedule

# Copy your script
COPY downloader.py ./downloader.py

CMD [ "python", "./downloader.py" ]
