# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log
from rosshm.db import reg
from rosshm.db.conn import DBConn
from rosshm.db.schema.schema import DBSchema
from rosshm.db.schema.status import DBStatus
from rosshm.db.schema.user import DBUser

__all__ = ['DatabaseError', 'IntegrityError', 'connect', 'status', 'create']

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

def status(conn):
	"""return database status table info"""
	s = DBStatus()
	return s.get(conn, 'status', pk = 1)

def create(conn, admin = None):
	"""create database schema"""
	meta = DBSchema()
	# init schema tracking table first
	log.debug(f"create tables {list(reg.DB.tables.keys())}")
	tbl = reg.DB.tables['core'].get(meta.table)
	assert tbl
	tbl.create(conn)
	# init the rest of them
	for tbl in reg.DB.tables['core'].values():
		if tbl.name != meta.table:
			tbl.create(conn)
		# save schema metadata
		meta.set(conn, object = tbl.name, version = tbl.version)
	# create admin user if provided
	if admin is not None:
		u = DBUser()
		u.set(conn, name = admin.username, fullname = 'admin user')
	# set db status
	s = DBStatus()
	s.set(conn, status = 'ok')
	return {}
