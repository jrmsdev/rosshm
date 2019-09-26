# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from datetime import datetime, timezone
from time import time

from rosshm import log

_birth = datetime(1980, 6, 21, 7, 30, tzinfo = timezone.utc)
_birth = _birth.strftime("%a, %d %b %Y %H:%M:%S %Z")

class Plugin(object):
	name = 'rosshm.response'
	api = 2

	def __init__(self, debug = False):
		self.debug = debug

	def setup(self, wapp):
		log.debug(f"setup {self.name}")

	def apply(self, callback, ctx):
		log.debug(f"apply {self.name}")

		def wrapper(*args, **kwargs):
			log.debug(f"apply wrapper {self.name}")

			start = None
			if self.debug:
				start = time()

			resp = callback(*args, **kwargs)
			bottle.response['Server'] = 'rosshm'

			csp = "object-src 'self';"
			csp += " default-src 'self';"
			csp += " script-src 'self';"
			bottle.response['Content-Security-Policy'] = csp

			cache = "no-cache; max-age=0"
			bottle.response['Cache-Control'] = cache

			expires = _birth
			bottle.response['Expires'] = expires

			if self.debug:
				bottle.response['X-Took'] = "%.7f" % (time() - start)

			return resp

		return wrapper
