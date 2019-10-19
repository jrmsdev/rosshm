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

#
# register db schema
#
def register(dbn, obj):
	if not DB.tables.get(dbn, False):
		DB.tables[dbn] = {}
	if DB.tables[dbn].get(obj.table, False):
		raise RuntimeError(f"db object {obj}: table {obj.table} already registered")
	DB.tables[dbn][obj.table] = DBTable(obj)
