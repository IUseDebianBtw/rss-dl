# rssDownloader

rss-dl is a simple docker based rss downloader

https://github.com/bossman7309/rss-dl/blob/7807d392aa5318cf9c8d95c727d9342e18a8040a/images/rss-dl-logo-grey.png

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
    image: bossman7309/rss-dl:latest
    container_name: rssDownloader
    environment:
      - RSS_FEED_URL=example.com
      - DOWNLOAD_DIR=/downloads
    volumes:
      - /portainer/Files/AppData/Config/rssDownloader:/downloads
    restart: unless-stopped
```
