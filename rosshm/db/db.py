# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log
from rosshm.db import reg
from rosshm.db.conn import DBConn
from rosshm.db.schema import DBSchema
from rosshm.db.table import DBTable

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
	# init schema tracking table first
	log.info(f"create {dbn} schema")
	meta = DBSchema()
	tbl = DBTable(meta)
	tbl.create(conn)
	meta.set(conn, object = tbl.name, version = tbl.version)
	# init the rest of the tables
	tables = list(reg.DB.tables[dbn].keys())
	log.debug(f"create {dbn} tables {tables}")
	for tbl in reg.DB.tables[dbn].values():
		log.info(f"create {dbn} table {tbl.name}")
		tbl.create(conn)
		meta.set(conn, object = tbl.name, version = tbl.version)
	return {}
