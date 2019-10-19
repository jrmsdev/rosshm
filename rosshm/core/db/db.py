# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.core.db.schema.status import DBStatus
from rosshm.core.db.schema.user import DBUser
from rosshm.db.reg import register

__all__ = ['status', 'initdb']

def status(conn):
	"""return database status table info"""
	s = DBStatus()
	return s.get(conn, 'status', pk = 1)

def initdb(conn, admin = None):
	"""initialize database schema"""
	# create admin user if provided
	if admin is not None:
		u = DBUser()
		u.set(conn, name = admin.username, fullname = 'admin user')
	# set db status
	s = DBStatus()
	s.set(conn, status = 'ok')
	return {}

register('core', initdb = initdb)
