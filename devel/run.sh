#!/bin/sh
exec rosshm --log debug --workers 1 --threads 1 \
	--config ./devel/rosshm.ini $@
