# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db import sql

__all__ = ['DBObject']

#
# object manager
#
class DBObject(object):
	table = None
	schema = None

	def __init__(self):
		self.fields = {}
		self.version = 0
		for v in sorted(self.schema.keys()):
			if v > self.version:
				self.version = v
			d = self.schema.get(v)
			self._loadFields(d)

	def _loadFields(self, data):
		for f, inf in data.items():
			# TODO: check field type, if it alters the table or what?
			self.fields[f] = inf

	def set(self, db, **data):
		stmt, args = sql.insert(self.table, self.fields, data)
		db.execute(stmt, args)

	def get(self, db, *filter, **where):
		stmt, args = sql.select(self.table, self.fields.keys(), filter, where)
		row = db.execute(stmt, args).fetchone()
		if row is None:
			return {}
		return row
