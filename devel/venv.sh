#!/usr/bin/env bash
ENVDIR=${1:-'/opt/venv/rosshmdev'}
PIP=${ENVDIR}/bin/pip
python3 -m venv --system-site-packages --symlinks --upgrade \
	--prompt rosshmdev ${ENVDIR}
${PIP} install -U pip
${PIP} install -U -r devel/requirements.txt
${PIP} install -U -r requirements.txt
${PIP} uninstall -y rosshm
${PIP} install -e .
