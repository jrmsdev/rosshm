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
def db_ctx(cfgfn = 'rosshm.ini', cfginit = True, create = True, db_t = False, close = True):
	conn = None
	with config_ctx(fn = cfgfn, init = cfginit) as config:
		dbcfg = config.database()
		conn = db.connect(dbcfg)
		if create:
			db.create(conn)
			if db_t:
				_t = DBTable(DBTesting())
				_t.create(conn)
		try:
				conn.commit()
				yield conn
		finally:
			if close and conn is not None:
				conn.close()
				del conn
