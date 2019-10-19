# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db import db
from rosshm.db.schema.status import DBStatus
from rosshm.db.schema.user import DBUser

__all__ = ['create', 'status']

def status(conn):
	"""return database status table info"""
	s = DBStatus()
	return s.get(conn, 'status', pk = 1)

def create(conn, admin = None):
	"""create database schema"""
	db.create('core', conn)
	# create admin user if provided
	if admin is not None:
		u = DBUser()
		u.set(conn, name = admin.username, fullname = 'admin user')
	# set db status
	s = DBStatus()
	s.set(conn, status = 'ok')
	return {}
