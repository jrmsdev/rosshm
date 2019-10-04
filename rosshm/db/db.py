# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log
from rosshm.db import reg
from rosshm.db.conn import DBConn
from rosshm.db.schema.schema import DBSchema
from rosshm.db.schema.status import DBStatus

__all__ = ['Error', 'connect', 'status', 'create']

Error = None
IntegrityError = None

def connect(cfg):
	global Error
	global IntegrityError
	conn = None
	drv = cfg.get('driver')
	if drv == 'sqlite':
		from rosshm.db.drv import sqlite
		Error = sqlite.Error
		IntegrityError = sqlite.IntegrityError
		conn = sqlite.connect(cfg)
	elif drv in ('mysql', 'mariadb'):
		from rosshm.db.drv import mysql
		Error = mysql.Error
		IntegrityError = mysql.IntegrityError
		conn = mysql.connect(cfg)
	else:
		raise RuntimeError(f"invalid database driver: {drv}")
	return DBConn(conn)

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
