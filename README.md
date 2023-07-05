# rssDownloader

version: "3.7"
services:
   rss-downloader:
    image: rss-downloader:latest
    container_name: rssDownloader
    environment:
     - RSS_FEED_URL: 'https://example.com/rss'
     - DOWNLOAD_DIR: '/downloads'
    volumes:
      - /portainer/Files/AppData/Config/rssDownloader:/downloads
    restart: unless-stopped
