# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from os import path
from unittest.mock import Mock

from testing.config_ctx import config_ctx
from testing.db_ctx import db_ctx

import bottle
import rosshm.wapp.wapp

class _bup:
	Bottle = bottle.Bottle

@contextmanager
def wapp_ctx(profile, cfgfn = 'rosshm.ini', db = False):
	cfgfn = path.join(profile, cfgfn)
	try:
		with config_ctx(fn = cfgfn) as config, _dbctx(db, cfgfn) as dbconn:
			yield _mock(config, dbconn)
	finally:
		del rosshm.wapp.wapp.bottle.Bottle
		rosshm.wapp.wapp.bottle.Bottle = _bup.Bottle

def _mock(config, dbconn):
	ctx = Mock()
	ctx.config = config
	ctx.dbconn = dbconn
	rosshm.wapp.wapp.bottle.Bottle = ctx.Bottle
	rosshm.wapp.wapp.bottle.Bottle.return_value = Mock()
	ctx.wapp = rosshm.wapp.wapp.init()
	return ctx

@contextmanager
def _nullctx():
	yield None

def _dbctx(enable, cfgfn):
	if enable:
		return db_ctx(cfgfn = cfgfn, cfginit = False)
	return _nullctx()
