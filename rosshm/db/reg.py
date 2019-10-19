# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.table import DBTable

__all__ = ['DB', 'register']

#
# db registry
#
_reg = {}

class DB(object):
	tables = {}
	init = {}

#
# register db schema
#
def register(obj = None, dbn = 'db', initdb = None):
	if initdb is not None:
		if DB.init.get(dbn, None) is not None:
			raise RuntimeError(f"{dbn} db init func already registered")
		DB.init[dbn] = initdb
	else:
		if obj.dbn is not None:
			dbn = obj.dbn
		if not DB.tables.get(dbn, False):
			DB.tables[dbn] = {}
		if DB.tables[dbn].get(obj.table, False):
			raise RuntimeError(f"{dbn} db object {obj}: table {obj.table} already registered")
		DB.tables[dbn][obj.table] = DBTable(obj)
