# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.obj import base

class DBStatus(base.DBObject):
	table = 'status'
	fields = {
		'status': (str, {'size': 64}),
	}

base.register(DBStatus())
