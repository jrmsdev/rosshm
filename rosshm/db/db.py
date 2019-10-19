# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log
from rosshm.db import reg
from rosshm.db.conn import DBConn
from rosshm.db.schema.schema import DBSchema

__all__ = ['DatabaseError', 'IntegrityError', 'connect', 'create']

DatabaseError = None
IntegrityError = None

def connect(cfg):
	"""return connection to configured database"""
	global DatabaseError
	global IntegrityError
	conn = None
	drv = cfg.get('driver')
	if drv == 'sqlite':
		from rosshm.db.drv import sqlite
		DatabaseError = sqlite.DatabaseError
		IntegrityError = sqlite.IntegrityError
		conn = sqlite.connect(cfg)
	elif drv in ('mysql', 'mariadb'):
		from rosshm.db.drv import mysql
		DatabaseError = mysql.DatabaseError
		IntegrityError = mysql.IntegrityError
		conn = mysql.connect(cfg)
	else:
		raise RuntimeError(f"invalid database driver: {drv}")
	return DBConn(conn)

def create(dbn, conn):
	"""create database schema"""
	meta = DBSchema()
	# init schema tracking table first
	log.debug(f"create tables {list(reg.DB.tables.keys())}")
	tbl = reg.DB.tables[dbn].get(meta.table)
	assert tbl
	tbl.create(conn)
	# init the rest of them
	for tbl in reg.DB.tables[dbn].values():
		if tbl.name != meta.table:
			tbl.create(conn)
		# save schema metadata
		meta.set(conn, object = tbl.name, version = tbl.version)
	return {}
