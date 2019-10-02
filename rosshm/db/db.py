# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

# register schema objects first
import rosshm.db.load

from rosshm import log
from rosshm.db import reg
from rosshm.db.schema.status import DBStatus

__all__ = ['Error', 'connect', 'status', 'create']

Error = sqlite3.OperationalError
IntegrityError = sqlite3.IntegrityError

def connect(cfg):
	fn = cfg.get('name')
	conn = sqlite3.connect(fn)
	conn.row_factory = sqlite3.Row
	return conn

def status(conn):
	s = DBStatus()
	return s.get(conn, 'status', pk = 0)

def create(conn):
	# init schema tracking table
	log.debug(f"create tables {list(reg.DB.tables.keys())}")
	tbl = reg.DB.tables.get('schema')
	assert tbl
	tbl.create(conn)
	# init the rest of them
	for tbl in reg.DB.tables.values():
		if tbl.name == 'schema': continue
		tbl.create(conn)
	# set db status
	s = DBStatus()
	s.set(conn, pk = 0, status = 'ok')
	conn.commit()
	return {}
