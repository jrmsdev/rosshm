# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['init']

from rosshm import log

def init(config, wapp):
	"""initialize web package"""
	log.debug(f"init {config.filename()}")
