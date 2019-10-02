# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db import sql

__all__ = ['DBTable']

#
# table manager
#
class DBTable(object):

	def __init__(self, obj):
		self.obj = obj

	def create(self, db):
		stmt = sql.createTable(self.obj.table, self.obj.fields)
		db.execute(stmt)
		db.commit()
