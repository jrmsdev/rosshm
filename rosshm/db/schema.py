# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.obj import DBObject

class DBSchema(DBObject):
	dbn = 'db'
	table = 'schema'
	schema = {
		0: {
			'object':  (str, {'size': 64, 'unique': True}),
			'version': (int, {}),
		},
	}
