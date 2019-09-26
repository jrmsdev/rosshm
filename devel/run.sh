#!/bin/sh
exec rosshm --debug --workers 1 --threads 1 --config ./devel/rosshm.ini $@
