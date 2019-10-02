# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.obj import DBObject
from rosshm.db.reg import register

class DBSchema(DBObject):
	table = 'schema'
	schema = {
		0: {
			'object':  (str, {'size': 64}),
			'version': (int, {}),
		},
	}

register(DBSchema())
