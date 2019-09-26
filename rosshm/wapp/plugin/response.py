# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from rosshm import log

class Plugin(object):
	name = 'rosshm.response'
	api = 2

	def setup(self, wapp):
		log.debug(f"setup {self.name}")

	def apply(self, callback, ctx):
		log.debug(f"apply {self.name}")
		def wrapper(*args, **kwargs):
			log.debug(f"apply wrapper {self.name}")
			bottle.response['Server'] = 'rosshm'
			return callback(*args, **kwargs)
		return wrapper
