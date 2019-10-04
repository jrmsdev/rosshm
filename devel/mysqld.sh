#!/bin/sh
docker run --rm -it -p 127.0.0.1:3306:3306 \
	-e MYSQL_ROOT_PASSWORD=rosshmpw \
	-e MYSQL_DATABASE=rosshmdb \
	-e MYSQL_USER=rosshm \
	-e MYSQL_PASSWORD=rosshmpw \
	mariadb
