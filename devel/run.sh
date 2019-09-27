#!/bin/sh
exec rosshm --workers 1 --threads 1 --config ./devel/rosshm.ini $@
