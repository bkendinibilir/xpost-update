REPO=bkendinibilir
NAME=xpost-update
VERSION=latest

build:
	docker build -t ${REPO}/${NAME} .

push:
	docker buildx build --platform linux/amd64,linux/arm64 --push -t ${REPO}/${NAME}:${VERSION} .

clean:
	docker rmi ${REPO}/${NAME}

all: clean build push
