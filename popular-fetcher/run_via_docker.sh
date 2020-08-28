(docker stop api-youtube-popular || :) && (docker rm api-youtube-popular || :)
docker run -d \
-p 8000:8000 \
--expose=8000 \
--name="api-youtube-popular" \
--restart=always \
youtubeapi:0.0.1-popular-fetcher