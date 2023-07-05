# rssDownloader

rss-dl is a simple rss downloader

creator:

https://github.com/bossman7309
https://bossman7309.net/

pi-hosted:

https://github.com/novaspirit/pi-hosted

docker compose:
```
version: "3.7"
services:
  rss-downloader:
    image: rss-downloader:latest
    container_name: rssDownloader
    environment:
      - RSS_FEED_URL=example.com
      - DOWNLOAD_DIR=/downloads
    volumes:
      - /portainer/Files/AppData/Config/rssDownloader:/downloads
    restart: unless-stopped
```
