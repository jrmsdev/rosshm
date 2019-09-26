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
			csp = "object-src 'self';"
			csp += " default-src 'self';"
			csp += " script-src 'self';"
			bottle.response['Content-Security-Policy'] = csp
			return callback(*args, **kwargs)
		return wrapper
