# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

from rosshm.db import sql

__all__ = ['register', 'DBObject']

#
# object manager
#
class DBObject(object):
	table = None
	fields = {}

	def set(self, db, **data):
		stmt, args = sql.insert(self.table, self.fields.keys(), data)
		db.execute(stmt, args)

	def get(self, db, where, filter):
		stmt, args = sql.select(self.table, self.fields.keys(), where, filter)
		row = db.execute(stmt, args).fetchone()
		return dict(row)

#
# table manager
#
class DBTable(object):

	def __init__(self, obj):
		self.obj = obj

	def create(self, db):
		stmt = sql.createTable(self.obj.table, self.obj.fields)
		db.execute(stmt)

#
# db manager
#
class DB(object):
	ok = {}
	tables = deque()

#
# register db schema
#
def register(obj):
	if DB.ok.get(obj.table, False):
		raise RuntimeError(f"db object {obj} table {obj.table} already registered")
	DB.tables.append(DBTable(obj))
	DB.ok[obj.table] = True
