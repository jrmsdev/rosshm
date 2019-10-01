#!/bin/sh -eu
PYTHONPATH=${PWD} pytest --cov=rosshm --cov-report=term --cov-report=html $@
exit 0
