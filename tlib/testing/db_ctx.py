# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock

from rosshm.db import db
from rosshm.db.table import DBTable

from testing.config_ctx import config_ctx
from testing.db.schema import DBTesting

__all__ = ['db_ctx']

@contextmanager
def db_ctx(create = True, db_t = False, close = True):
	conn = None
	with config_ctx() as cfg:
		cfg.set('rosshm', 'db.driver', 'sqlite')
		cfg.set('rosshm', 'db.name', ':memory:')
		if create:
			dbcfg = {'driver': 'sqlite', 'name': ':memory:', 'config': ''}
			conn = db.connect(dbcfg)
			db.create(conn)
			if db_t:
				_t = DBTable(DBTesting())
				_t.create(conn)
		try:
				yield conn
		finally:
			if close and conn is not None:
				conn.close()
				del conn
				conn = None
