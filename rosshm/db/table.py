# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log
from rosshm.db import sql

__all__ = ['DBTable']

#
# table manager
#
class DBTable(object):

	def __init__(self, obj):
		self.name = obj.table
		self.fields = obj.fields
		self.version = obj.version

	def create(self, db):
		log.debug(f"create {self.name}")
		stmt = sql.createTable(self.name, self.fields)
		db.execute(stmt)
		log.debug('commit changes')
		db.commit()
