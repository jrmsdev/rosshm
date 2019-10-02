# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

from contextlib import contextmanager
from os import path
from pathlib import Path

from rosshm import config

__all__ = ['testing_config']

tdata = Path(path.abspath(path.join('.', 'tdata')))

@contextmanager
def config_ctx(fn = 'rosshm.ini'):
	cfg = config._cfg
	try:
		fn = str(tdata / fn)
		config.init(fn = fn)
		assert config._cfgfn == fn, f"{fn} config file not read"
		yield config._cfg
	finally:
		config._cfg = cfg
		config._cfgfn = None

@pytest.fixture
def testing_config():
	return config_ctx
