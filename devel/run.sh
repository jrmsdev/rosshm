#!/bin/sh
exec python3 ${PWD}/rosshm/cmd/main.py --log debug --config ./devel/rosshm.ini $@
