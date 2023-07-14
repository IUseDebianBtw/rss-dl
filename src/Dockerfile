FROM python:3.8-slim

WORKDIR /app

# Set Environment Variables
ENV CHANNEL_URL=https://youtube.com/@MentalOutlaw
ENV DOWNLOAD_PATH=/app/downloads

# Copy your scripts
COPY ./src /app/src
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

CMD [ "python", "-m", "src.main" ]