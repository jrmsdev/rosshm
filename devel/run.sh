#!/bin/sh
exec python3 ./rosshm/cmd/main.py --log debug --config ./devel/rosshm.ini $@
