# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db import sql

__all__ = ['DBObject']

#
# object manager
#
class DBObject(object):
	table = None
	fields = {}

	def set(self, db, **data):
		stmt, args = sql.insert(self.table, self.fields.keys(), data)
		db.execute(stmt, args)

	def get(self, db, *filter, **where):
		stmt, args = sql.select(self.table, self.fields.keys(), filter, where)
		row = db.execute(stmt, args).fetchone()
		return dict(row)
