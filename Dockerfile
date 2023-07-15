FROM python:3.8-slim

WORKDIR /app

# Set Environment Variables
ENV CHANNEL_URLS=https://youtube.com/@MentalOutlaw,https://www.youtube.com/@HiddenXperia,https://www.youtube.com/@TheActMan

# Copy your scripts
COPY ./src /app/src

# Copy requirements.txt from the project root into the Docker image
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r /app/requirements.txt

CMD [ "python", "-m", "src.main" ]