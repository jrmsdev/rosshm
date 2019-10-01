# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from rosshm import log
from rosshm.db import db

class DBPlugin(object):
	name = 'rosshm.db'
	api = 2

	def __init__(self, dbfn, debug = False):
		self.dbfn = dbfn
		self.debug = debug

	def setup(self, wapp):
		log.debug(f"setup {self.name}")

	def apply(self, callback, ctx):
		log.debug(f"apply {ctx.name}")
		def wrapper(*args, **kwargs):
			log.debug(f"wrapper {ctx.name}")
			conn = db.connect(self.dbfn)
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
