# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from rosshm.db.obj.status import DBStatus

__all__ = ['connect', 'status']

def connect(fn):
	conn = sqlite3.connect(fn)
	conn.row_factory = sqlite3.Row
	return conn

def status(db):
	s = DBStatus()
	return s.get(db, {'pk': 0}, ('status',))
