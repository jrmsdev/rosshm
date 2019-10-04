# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from rosshm import log
from rosshm.db import reg
from rosshm.db.schema.schema import DBSchema
from rosshm.db.schema.status import DBStatus

__all__ = ['Error', 'connect', 'status', 'create']

Error = None
IntegrityError = None

def connect(cfg):
	global Error
	global IntegrityError
	drv = cfg.get('driver')
	if drv in ('mysql', 'mariadb'):
		import MySQLdb
		Error = MySQLdb.OperationalError
		IntegrityError = MySQLdb.IntegrityError
		return MySQLdb.connect(
			host = cfg.get('host', 'localhost'),
		)
	else:
		Error = sqlite3.OperationalError
		IntegrityError = sqlite3.IntegrityError
		fn = cfg.get('name')
		conn = sqlite3.connect(fn)
		conn.row_factory = sqlite3.Row
		return conn

def status(conn):
	s = DBStatus()
	return s.get(conn, 'status', pk = 0)

def create(conn):
	meta = DBSchema()
	# init schema tracking table first
	log.debug(f"create tables {list(reg.DB.tables.keys())}")
	tbl = reg.DB.tables.get(meta.table)
	assert tbl
	tbl.create(conn)
	# init the rest of them
	for tbl in reg.DB.tables.values():
		if tbl.name != meta.table:
			tbl.create(conn)
		# save schema metadata
		meta.set(conn, object = tbl.name, version = tbl.version)
	# set db status
	s = DBStatus()
	s.set(conn, pk = 0, status = 'ok')
	conn.commit()
	return {}
