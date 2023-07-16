FROM python:3.8-slim

WORKDIR /app

# Set Environment Variables
ENV CHANNEL_URL=https://youtube.com/@MentalOutlaw
ENV DOWNLOAD_PATH=/media/bossman7309/ORANGEHHD/uploads

# Copy your scripts
COPY ./src /app/src

# Install dependencies
RUN pip install -r feedparser, schedule, yt-dlp, schedule, requests

CMD [ "python", "-m", "src.main" ]
