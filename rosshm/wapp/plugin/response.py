# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from datetime import datetime, timezone
from time import time

from rosshm import log

_birth = datetime(2019, 9, 21, 3, 5, 38, tzinfo = timezone.utc)
# ~ _birth = _birth.strftime("%a, %d %b %Y %H:%M:%S %Z")

class Plugin(object):
	name = 'rosshm.response'
	api = 2

	def __init__(self, debug = False):
		self.debug = debug

	def setup(self, wapp):
		log.debug(f"setup {self.name}")

	def apply(self, callback, ctx):
		log.debug(f"apply {ctx.name}")
		def wrapper(*args, **kwargs):
			log.debug(f"wrapper {ctx.name}")
			start = None
			if self.debug:
				start = time()
			resp = callback(*args, **kwargs)
			if isinstance(resp, bottle.HTTPResponse):
				self._setHeaders(resp, start)
			else:
				self._setHeaders(bottle.response, start)
			return resp
		return wrapper

	def _setHeaders(self, resp, start):
		# Server
		resp.set_header('Server', 'rosshm')
		# CSP
		csp = "object-src 'self';"
		csp += " default-src 'self';"
		csp += " script-src 'self';"
		resp.set_header('Content-Security-Policy', csp)
		# Cache-Control
		cache = "no-cache; max-age=0"
		resp.set_header('Cache-Control', cache)
		# Expires
		resp.expires = _birth
		# debug info
		if self.debug:
			resp.set_header('X-Took', "%.7f" % (time() - start))
