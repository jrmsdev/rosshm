# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from os import path
from unittest.mock import Mock

from testing.config_ctx import config_ctx

import rosshm.wapp.wapp

@contextmanager
def wapp_ctx(profile, cfgfn = 'rosshm.ini'):
	cfgfn = path.join(profile, cfgfn)
	try:
		with config_ctx(fn = cfgfn) as config:
			config._cfg.set('rosshm', 'db.driver', 'sqlite')
			config._cfg.set('rosshm', 'db.name', ':memory:')
			config._cfg.set('rosshm', 'db.config', '')
			ctx = Mock()
			ctx.config = config
			ctx.wapp = rosshm.wapp.wapp
			yield ctx
	finally:
		pass
