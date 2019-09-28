# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db import sql

class DBObject(object):
	table = None
	fields = {}

	def get(self, db, where, filter):
		stmt, args = sql.select(self.table, self.fields.keys(), where, filter)
		return db.execute(stmt, args).fetchone()
