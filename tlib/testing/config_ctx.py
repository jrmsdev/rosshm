# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager

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
		else:
			config._cfgfn = fn
		yield config._cfg
	finally:
		del config._cfg
		config._cfg = config._new()
		del config._cfgfn
		config._cfgfn = None
