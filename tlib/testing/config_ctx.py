# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock

from rosshm import config
from testing import tdata

__all__ = ['config_ctx']

@contextmanager
def config_ctx(fn = 'rosshm.ini', init = True):
	try:
		fn = str(tdata / fn)
		if init:
			config.init(fn = fn)
			assert config._cfgfn == fn, \
				f"config file not read: got: {config._cfgfn} - expect: {fn}"
			config.init_real = config.init
			config.init = Mock()
		else:
			config._cfgfn = fn
		yield config
	finally:
		del config._cfg
		config._cfg = config._new()
		del config._cfgfn
		config._cfgfn = None
		if init:
			del config.init
			config.init = config.init_real
			del config.init_real
