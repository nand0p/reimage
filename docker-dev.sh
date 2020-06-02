#!/bin/sh -ex

docker network create -d bridge reimage 2> /dev/null || true

docker build -t reimage-dev \
	     -f Dockerfile \
	     --build-arg "DATE=$(date)" \
	     --build-arg "REVISION=$(git rev-parse HEAD)" \
	     --build-arg "GOOGLE_API_KEY=$GOOGLE_API_KEY" \
	     --build-arg "GOOGLE_SEARCH_ID=$GOOGLE_SEARCH_ID" \
	     .

docker kill reimage-dev 2> /dev/null || true
sleep 2

docker run --rm --name reimage-dev -d --network=reimage -p 5004:5000 reimage-dev
sleep 5
docker ps

docker logs reimage-dev
echo "docker run --rm --name reimage-dev -ti -p 5004:8000 reimage-dev bash"
