# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from unittest.mock import Mock

from rosshm import config
from rosshm.db import db
from rosshm.db.reg import register

def test_config(testing_db):
	with testing_db(create = False) as conn:
		cfg = config.database()
		assert cfg['driver'] == 'sqlite'
		assert cfg['config'] == ''
		assert cfg['name'] == ':memory:'
		assert conn is None

def test_create(testing_db):
	with testing_db() as conn:
		row = db.status(conn)
		assert row['status'] == 'ok'

def test_register_error(testing_db):
	with testing_db(create = False):
		obj = Mock()
		obj.table = 'schema'
		with raises(RuntimeError, match = 'table schema already registered'):
			register(obj)
