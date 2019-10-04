# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest
from contextlib import contextmanager
from unittest.mock import Mock

from rosshm.db import db
from testing.config_ctx import config_ctx

__all__ = ['testing_db', 'db_ctx']

@contextmanager
def db_ctx(create = True):
	try:
		with config_ctx() as cfg:
			cfg.set('rosshm', 'db.driver', 'sqlite')
			cfg.set('rosshm', 'db.name', ':memory:')
			conn = None
			if create:
				dbcfg = {'driver': 'sqlite', 'name': ':memory:', 'config': ''}
				conn = db.connect(dbcfg)
				db.create(conn)
			yield conn
	finally:
		if conn is not None:
			conn.close()
		del conn
		conn = None

@pytest.fixture
def testing_db():
	return db_ctx
