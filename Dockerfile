FROM python:3.8-slim

WORKDIR /app

# Set Environment Variables
ENV CHANNEL_URL=https://youtube.com/@MentalOutlaw
ENV DOWNLOAD_PATH=/app/downloads

# Copy your scripts
COPY ./src /app/src

# Copy requirements.txt from the project root into the Docker image
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r /app/requirements.txt

CMD [ "python", "-m", "src.main" ]
