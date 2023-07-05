# rssDownloader


```
version: "3.7"
services:
  rss-downloader:
    image: rss-downloader:latest
    container_name: rssDownloader
    environment:
      - RSS_FEED_URL=https://rss.art19.com/part-of-the-problem
      - DOWNLOAD_DIR=/downloads
    volumes:
      - /portainer/Files/AppData/Config/rssDownloader:/downloads
    restart: unless-stopped

```
