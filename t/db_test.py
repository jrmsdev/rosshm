# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from pytest import raises
from unittest.mock import Mock

from rosshm import config
from rosshm.core.db import check
from rosshm.core.db.check import checkdb
from rosshm.db import db
from rosshm.db.reg import register

def test_config(testing_db):
	with testing_db(create = False) as conn:
		cfg = config.database()
		assert cfg['driver'] == 'sqlite'
		assert cfg['config'] == ''
		assert cfg['name'] == ':memory:'
		assert conn is not None

def test_create(testing_db):
	with testing_db() as conn:
		row = db.status(conn)
		assert row['status'] == 'ok'

def test_register_error(testing_db):
	with testing_db(create = False):
		obj = Mock()
		obj.table = 'schema'
		with raises(RuntimeError, match = 'table schema already registered'):
			register('core', obj)

def test_checkdb(testing_db):
	with testing_db(create = False):
		assert not checkdb(config)
	with testing_db(close = False) as conn:
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
		status = check.db.status
		try:
			check.db.status = Mock(return_value = None)
			assert not checkdb(config, conn = conn)
		finally:
			del check.db.status
			check.db.status = status

def test_invalid_driver():
	cfg = {'driver': 'nodrv', 'name': 'testing', 'config': ''}
	with raises(RuntimeError, match = 'invalid database driver: nodrv'):
		db.connect(cfg)

def test_conn_rollback(testing_db):
	with testing_db() as conn:
		conn.rollback()

def test_del_close(testing_db):
	with testing_db(close = False) as conn:
		assert not conn._closed
		conn.__del__()
		assert conn._closed
