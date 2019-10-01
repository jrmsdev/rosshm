# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.table import DBTable

__all__ = ['DB', 'register']

#
# db registry
#
class DB(object):
	tables = {}

#
# register db schema
#
def register(obj):
	if DB.tables.get(obj.table, False):
		raise RuntimeError(f"db object {obj}: table {obj.table} already registered")
	DB.tables[obj.table] = DBTable(obj)
