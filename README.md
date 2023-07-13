# rssDownloader

rss-dl is a simple docker based rss downloader

![Logo](./images/rss-dl-logo-grey.png)

https://git.bossman7309.net/

creator:

https://github.com/bossman7309
https://bossman7309.net/

pi-hosted:

https://github.com/novaspirit/pi-hosted

docker pull bossman7309/rss-dl

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
