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
	dbconn = None
	wapp = None

	def __init__(self, config, dbconn):
		self.config = config
		self.dbconn = dbconn

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
def wapp_ctx(profile, cfgfn = 'rosshm.ini', db = False):
	cfgfn = path.join(profile, cfgfn)
	try:
		with config_ctx(fn = cfgfn) as config, _dbctx(db, cfgfn) as dbconn:
			ctx = WappCtx(config, dbconn)
			ctx.wapp = rosshm.wapp.wapp.init()
			yield ctx
	finally:
		pass

@contextmanager
def _nullctx():
	yield None

def _dbctx(enable, cfgfn):
	if enable:
		return db_ctx(cfgfn = cfgfn, cfginit = False)
	return _nullctx()
