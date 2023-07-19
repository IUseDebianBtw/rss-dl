FROM python:3.8-slim

WORKDIR /app

# Set Environment Variables
ENV CHANNEL_URL=https://www.youtube.com/@Fireship
ENV ENV DOWNLOAD_PATH=/app/downloads

# Copy your scripts
COPY main.py ./main.py
COPY video_downloader.py ./video_downloader.py
COPY directory_setup.py ./directory_setup.py
COPY ascii_art.txt ./ascii_art.txt
COPY __init__.py ./__init__.py

# Install dependencies
RUN pip install feedparser schedule yt-dlp requests

CMD [ "python", "-m", "main" ]