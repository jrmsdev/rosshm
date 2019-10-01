# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from rosshm.db.schema.status import DBStatus
from rosshm.db.reg import DB

__all__ = ['Error', 'connect', 'status', 'create']

#
# load/register db schema objects
#
import rosshm.db.load

Error = sqlite3.OperationalError

def connect(fn):
	conn = sqlite3.connect(fn)
	conn.row_factory = sqlite3.Row
	return conn

def status(conn):
	s = DBStatus()
	return s.get(conn, 'status', pk = 0)

def create(conn):
	for tbl in DB.tables.values():
		tbl.create(conn)
	s = DBStatus()
	s.set(conn, pk = 0, status = 'ok')
	conn.commit()
	return {}
