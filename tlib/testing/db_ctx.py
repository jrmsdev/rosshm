# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from os import path
from unittest.mock import Mock

from rosshm.db import db
from rosshm.db.reg import register

from testing.config_ctx import config_ctx
from testing.db.schema import DBTesting

__all__ = ['db_ctx']

register(obj = DBTesting())

@contextmanager
def db_ctx(cfgfn = 'rosshm.ini', cfginit = True, create = True, db_t = False,
	close = True, dbn = 'testing'):
	conn = None
	if dbn != 'testing':
		cfgfn = path.join(dbn, cfgfn)
	with config_ctx(fn = cfgfn, init = cfginit) as config:
		dbcfg = config.database()
		conn = db.connect(dbcfg)
		dbn = config.get('testing.dbn', dbn)
		if create:
			db.create(dbn, conn)
			if db_t:
				_t = DBTesting()
				_t.dbn = dbn
				_t.set(conn, value = 'testing', option = 'testing')
			conn.commit()
		try:
			yield conn
		finally:
			if close and conn is not None:
				conn.commit()
				conn.close()
				del conn
