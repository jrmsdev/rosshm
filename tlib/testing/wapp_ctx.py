# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock

from testing.config_ctx import config_ctx

import rosshm.wapp.wapp

@contextmanager
def wapp_ctx(cfgfn = 'rosshm.ini'):
	try:
		with config_ctx(fn = cfgfn) as cfg:
			ctx = Mock()
			ctx.cfg = cfg
			ctx.wapp = rosshm.wapp.wapp
			yield ctx
	finally:
		pass
