# Select base image
FROM python:3.7-alpine3.11

# Add note
LABEL name="PatharaNor"
LABEL version="0.0.1"

# Create folder in container
WORKDIR /app

# Copy dependencies list to container
COPY ./requirements.txt .

# Update and install library if need
RUN apk update \
    && apk add --no-cache jpeg-dev zlib-dev libjpeg \
    && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev build-base linux-headers \
    && pip3 install -r requirements.txt \
    && apk del build-deps \
    && rm -rf /var/cache/apk/*

# Bundle code to container
COPY . .

# Open container port
EXPOSE 8000

# Run startup script
CMD ["sh", "run.sh"]