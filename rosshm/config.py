# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import getenv, path

def init(fn = None):
	if fn is None:
		fn = getenv('ROSSHM_CONFIG',
			path.expanduser(path.join('~', '.config', 'rosshm.ini')))
