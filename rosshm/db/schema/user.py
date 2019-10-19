# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.obj import DBObject
from rosshm.db.reg import register

class DBUser(DBObject):
	table = 'user'
	schema = {
		0: {
			'name': (str, {'size': 64}),
			'fullname': (str, {'size': 256}),
		},
	}

register('core', DBUser())
