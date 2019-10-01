# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

from rosshm.db.obj.status import DBStatus
from rosshm.db.table import DBTable

#
# db registry
#
class DB(object):
	ok = {}
	tables = deque()

#
# register db schema
#
def register(obj):
	if DB.ok.get(obj.table, False):
		raise RuntimeError(f"db object {obj}: table {obj.table} already registered")
	DB.tables.append(DBTable(obj))
	DB.ok[obj.table] = True

register(DBStatus())
