# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

from contextlib import contextmanager
from os import environ, path
from pathlib import Path
from unittest.mock import Mock

# set testing os environ
_osenv = {
	'ROSSHM_CONFIG': '',
	'ROSSHM_HOME': path.join(path.sep, 'opt', 'rosshm'),
}
for k, v in _osenv.items():
	environ.setdefault(k, v)
	environ[k] = v

# test data paths manager
tdata = Path(path.abspath(path.join('.', 'tdata')))

# export fixtures
__all__ = ['testing_config', 'testing_cmd']

#
# config
#

from rosshm import config

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

#
# cmd
#

from rosshm.cmd import main as cmd_main

@contextmanager
def cmd_ctx():
	proc = cmd_main.proc
	wapp = cmd_main.wapp
	with config_ctx():
		try:
			cmd_main.proc.run = Mock()
			cmd_main.wapp = Mock()
			cmd_main.wapp.init = Mock()
			cmd_main.wapp.mock_app = Mock()
			cmd_main.wapp.init.return_value = cmd_main.wapp.mock_app
			yield cmd_main
		finally:
			cmd_main.proc = proc
			cmd_main.wapp = wapp

@pytest.fixture
def testing_cmd():
	return cmd_ctx
