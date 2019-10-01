# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.obj.base import DBObject

class DBStatus(DBObject):
	table = 'status'
	fields = {
		'status': (str, {'size': 64}),
	}
