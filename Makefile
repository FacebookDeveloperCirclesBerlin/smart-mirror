run:
	docker run -i -t --rm -e DISPLAY=host.docker.internal:0 -e TZ=Europe/Berlin -v /tmp/.X11-unix:/tmp/.X11-unix:ro --name="weysan-smart-mirror" weysan/smart-mirror

build:
	docker build -t weysan/smart-mirror .

run-last: build run

tests:
	pytest
