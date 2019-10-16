# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from os import path
from unittest.mock import Mock

from testing.config_ctx import config_ctx

import bottle
import rosshm.wapp.wapp

class _bup:
	Bottle = bottle.Bottle

@contextmanager
def wapp_ctx(profile, cfgfn = 'rosshm.ini'):
	cfgfn = path.join(profile, cfgfn)
	try:
		with config_ctx(fn = cfgfn) as config:
			config._cfg.set('rosshm', 'db.driver', 'sqlite')
			config._cfg.set('rosshm', 'db.name', ':memory:')
			config._cfg.set('rosshm', 'db.config', '')
			yield _mock(config)
	finally:
		del rosshm.wapp.wapp.bottle.Bottle
		rosshm.wapp.wapp.bottle.Bottle = _bup.Bottle

def _mock(config):
	ctx = Mock()
	ctx.config = config
	rosshm.wapp.wapp.bottle.Bottle = ctx.Bottle
	rosshm.wapp.wapp.bottle.Bottle.return_value = Mock()
	ctx.wapp = rosshm.wapp.wapp.init()
	return ctx
