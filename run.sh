#!/bin/bash

# 이미지 지정
IMAGE_NAME=$1
if [ -z "$IMAGE_NAME" ]; then
    echo "Image name must be specified"
    exit 1
fi

# 도커 컨테이너 실행
docker run -d \
    --name wisdom-app-client \
    --network wisdom-app-net \
    -p 8501:8501 \
    -v $(pwd):/usr/src/app \
    --env-file .env \
    --restart unless-stopped \
    -v $(pwd):/usr/src/app \
    -w /usr/src/app \
    --log-driver json-file \
    --log-opt max-size=10m \
    --log-opt max-file=5 \
    $IMAGE_NAME
