# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest
from contextlib import contextmanager

from rosshm import config
from testing import tdata

__all__ = ['testing_config', 'config_ctx']

@contextmanager
def config_ctx(fn = 'rosshm.ini'):
	cfg = config._cfg
	try:
		fn = str(tdata / fn)
		config.init(fn = fn)
		assert config._cfgfn == fn, \
			f"config file not read: got: {config._cfgfn} - expect: {fn}"
		yield config._cfg
	finally:
		config._cfg = cfg
		config._cfgfn = None

@pytest.fixture
def testing_config():
	return config_ctx
