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

def create(dbn, conn, **initdb_args):
	"""create database schema"""
	# create schema tracking table first
	log.info(f"create {dbn} schema")
	meta = DBSchema()
	meta.dbn = dbn
	tbl = DBTable(meta)
	tbl.create(conn)
	meta.set(conn, object = tbl.name, version = tbl.version)
	# create the rest of the tables
	tables = list(reg.DB.tables[dbn].keys())
	log.debug(f"create {dbn} tables {tables}")
	for tbl in reg.DB.tables[dbn].values():
		log.info(f"create {dbn} table {tbl.name}")
		tbl.create(conn)
		meta.set(conn, object = tbl.name, version = tbl.version)
	# initialize database
	initdb = reg.DB.init.get(dbn, None)
	if initdb is not None:
		initdb(conn, **initdb_args)
	return {}
