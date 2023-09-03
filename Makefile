REPO=bkendinibilir
NAME=xpost-update
VERSION=latest

build:
	docker build -t ${REPO}/${NAME} .

push: build
	docker push ${REPO}/${NAME}:${VERSION}

clean:
	docker rmi ${REPO}/${NAME}

all: clean build push
