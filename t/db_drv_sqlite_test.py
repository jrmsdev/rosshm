# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import makedirs, path
from shutil import rmtree

_dbdir = path.join('tdata', 'var', 'sqlite')
_dbfn = path.join(_dbdir, 'rosshm.sqlite')

def test_connect(testing_db):
	try:
		makedirs(_dbdir, mode = 0o0700, exist_ok = True)
		with testing_db('sqlite.ini') as conn:
			pass
	finally:
		rmtree(_dbdir)
