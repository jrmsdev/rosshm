# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

from contextlib import contextmanager
from os import environ, path
from pathlib import Path

# set testing os environ
_osenv = {
	'ROSSHM_CONFIG': '',
	'ROSSHM_HOME': '',
}
for k, v in _osenv.items():
	environ.setdefault(k, v)
	environ[k] = v

from rosshm import config

__all__ = ['testing_config']

tdata = Path(path.abspath(path.join('.', 'tdata')))

#
# config
#
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
