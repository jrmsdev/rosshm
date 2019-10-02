# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.obj import DBObject
from rosshm.db.reg import register

class DBStatus(DBObject):
	table = 'status'
	schema = {
		0: {
			'status': (str, {'size': 64}),
		},
	}

register(DBStatus())
