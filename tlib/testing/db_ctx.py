# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock

from rosshm.core.db import db as coredb
from rosshm.db import db
from rosshm.db.reg import register

from testing.config_ctx import config_ctx
from testing.db.schema import DBTesting

__all__ = ['db_ctx']

register('testing', DBTesting())

@contextmanager
def db_ctx(cfgfn = 'rosshm.ini', cfginit = True, create = True, db_t = False, close = True):
	conn = None
	with config_ctx(fn = cfgfn, init = cfginit) as config:
		dbcfg = config.database()
		conn = db.connect(dbcfg)
		dbn = config.get('testing.dbn', 'testing')
		if create:
			if dbn == 'core':
				coredb.create(conn)
			else:
				db.create(dbn, conn)
			if db_t:
				_t = DBTesting()
				_t.set(conn, value = 'testing', option = 'testing')
			conn.commit()
		try:
			yield conn
		finally:
			if close and conn is not None:
				conn.commit()
				conn.close()
				del conn
