# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from rosshm import log
from rosshm.db import db

class DBPlugin(object):
	name = 'rosshm.db'
	api = 2

	def __init__(self, cfg, debug = False):
		self.cfg = cfg
		self.debug = debug

	def setup(self, wapp):
		# the plugin is not installed globally so this should never run
		log.debug(f"setup {self.name}")

	def apply(self, callback, ctx):
		log.debug(f"apply {ctx.name}")
		def wrapper(*args, **kwargs):
			log.debug(f"wrapper {ctx.name}")
			conn = db.connect(self.cfg)
			kwargs['db'] = conn
			try:
				resp = callback(*args, **kwargs)
				conn.commit()
			except db.IntegrityError as err:
				log.error(str(err))
				conn.rollback()
				raise bottle.HTTPError(500, "database error", err)
			finally:
				conn.close()
			return resp
		return wrapper
