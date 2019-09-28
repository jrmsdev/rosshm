# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from rosshm.db.obj.base import DB
from rosshm.db.obj.status import DBStatus

__all__ = ['Error', 'connect', 'status']

Error = sqlite3.OperationalError

def connect(fn):
	conn = sqlite3.connect(fn)
	conn.row_factory = sqlite3.Row
	return conn

def status(db):
	s = DBStatus()
	return s.get(db, {'pk': 0}, ('status',))

def create(db):
	for tbl in DB.tables:
		tbl.create(db)
	return {}
