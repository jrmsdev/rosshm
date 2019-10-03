# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import config
from rosshm.db import db

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
