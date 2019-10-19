# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from pytest import raises

from rosshm import config
from rosshm.db import db
from rosshm.db.reg import register

from testing.db.schema import DBTesting

db_t = DBTesting()

def test_config(testing_db):
	with testing_db(create = False) as conn:
		cfg = config.database()
		assert cfg['driver'] == 'sqlite'
		assert cfg['config'] == ''
		assert cfg['name'] == ':memory:'
		assert conn is not None

def test_create(testing_db):
	with testing_db(db_t = True) as conn:
		row = db_t.get(conn, 'value', option = 'testing')
		assert row['value'] == 'testing'

def test_register_error(testing_db):
	with testing_db(db_t = True):
		with raises(RuntimeError, match = 'table testing already registered'):
			register(db_t)

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
