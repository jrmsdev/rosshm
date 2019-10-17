# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

from os import environ, path, unlink

# cleanup build/dist files
for fn in ('_version.py', '_version_build.py'):
	fn = path.join('rosshm', fn)
	if path.isfile(fn):
		unlink(fn)

# set testing os environ
_osenv = {
	'ROSSHM_CONFIG': '',
	'ROSSHM_HOME': path.join(path.sep, 'opt', 'rosshm'),
}
for k, v in _osenv.items():
	environ.setdefault(k, v)
	environ[k] = v

# export fixtures

__all__ = [
	'testing_cmd',
	'testing_config',
	'testing_db',
	'testing_log',
	'testing_wapp',
	'testing_wapp_plugin',
]

from testing.cmd_ctx import cmd_ctx

@pytest.fixture
def testing_cmd():
	return cmd_ctx

from testing.config_ctx import config_ctx

@pytest.fixture
def testing_config():
	return config_ctx

from testing.db_ctx import db_ctx

@pytest.fixture
def testing_db():
	return db_ctx

from testing.log_ctx import log_ctx

@pytest.fixture
def testing_log():
	return log_ctx

from testing.wapp_ctx import wapp_ctx

@pytest.fixture
def testing_wapp():
	return wapp_ctx

from testing.wapp_plugin_ctx import wapp_plugin_ctx

@pytest.fixture
def testing_wapp_plugin():
	return wapp_plugin_ctx
