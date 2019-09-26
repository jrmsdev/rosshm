# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['init']

from rosshm import log
from rosshm.core.view import status

def init(config, wapp):
	log.debug(f"init {config.filename()}")
	wapp.route('/_/', 'GET', status.view, name = 'core.status')
