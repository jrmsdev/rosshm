# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from unittest.mock import Mock

from rosshm import config
from rosshm.core.db import check
from rosshm.core.db.check import checkdb

def test_checkdb(testing_db):
	with testing_db(dbn = 'core', create = False):
		assert not checkdb(config)
	with testing_db(dbn = 'core', close = False) as conn:
		assert checkdb(config, conn = conn)

def test_checkdb_makedirs(testing_db):
	with testing_db(close = False) as conn:
		makedirs = check.makedirs
		isfile = check.path.isfile
		try:
			datadir = path.join(path.sep, 'testing')
			check.makedirs = Mock()
			check.path.isfile = Mock(return_value = False)
			config._cfg.set('rosshm', 'datadir', datadir)
			config._cfg.set('rosshm', 'db.name', 'testing.db')
			checkdb(config, conn = conn)
			check.path.isfile.assert_called_with(path.join(datadir, 'testing.db.sqlite'))
			check.makedirs.assert_called_with(datadir, exist_ok = True, mode = 0o750)
		finally:
			del check.makedirs
			check.makedirs = makedirs
			del check.path.isfile
			check.path.isfile = isfile

def test_checkdb_no_status(testing_db):
	with testing_db(close = False) as conn:
		status = check.coredb.status
		try:
			check.coredb.status = Mock(return_value = None)
			assert not checkdb(config, conn = conn)
		finally:
			del check.coredb.status
			check.coredb.status = status
