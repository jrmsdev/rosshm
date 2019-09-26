#!/bin/sh
exec python3 ${PWD}/rosshm/cmd/main.py --log debug \
	--workers 1 --threads 1 --config ./devel/rosshm.ini $@
