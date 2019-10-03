# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import environ, path

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
]

from testing.cmd    import testing_cmd
from testing.config import testing_config
from testing.db     import testing_db
