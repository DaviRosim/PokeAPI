.PHONY: build run clean

build:
	docker-compose build --no-cache

run: build
	docker-compose up

clean:
	docker-compose down
	docker image prune -f