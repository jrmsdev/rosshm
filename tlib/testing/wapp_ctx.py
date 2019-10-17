# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from contextlib import contextmanager
from os import path
from unittest.mock import Mock

from testing.config_ctx import config_ctx
from testing.db_ctx import db_ctx

import rosshm.wapp.wapp

class WappCtx(object):
	"""wapp context manager"""
	config = None
	db = None
	wapp = None

	def __init__(self, config, dbconn):
		self.config = config
		self.db = dbconn

	def request(self, method = 'GET', path = '/', qs = ''):
		env = {
			'REQUEST_METHOD': method,
			'PATH_INFO': path,
			'QUERY_STRING': qs,
		}
		req = bottle.LocalRequest(environ = env)
		assert req.method == method
		assert req.path == path
		return req

	@contextmanager
	def redirect(self, location, code = 302):
		try:
			yield
		except bottle.HTTPResponse as resp:
			loc = resp.headers.get('location', 'NOTSET')
			print('RESP:', resp.status_code, loc)
			assert resp.status_code == code
			assert loc.endswith(location)

@contextmanager
def wapp_ctx(profile, cfgfn = 'rosshm.ini', db = False, dbcreate = True):
	cfgfn = path.join(profile, cfgfn)
	with config_ctx(fn = cfgfn) as config, _dbctx(db, cfgfn, dbcreate) as dbconn:
		ctx = WappCtx(config, dbconn)
		ctx.wapp = rosshm.wapp.wapp.init()
		yield ctx

@contextmanager
def _nullctx():
	yield None

def _dbctx(enable, cfgfn, create):
	if enable:
		return db_ctx(cfgfn = cfgfn, cfginit = False, create = create)
	return _nullctx()
