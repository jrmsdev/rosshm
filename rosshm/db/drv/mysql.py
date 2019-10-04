# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import MySQLdb

Error = MySQLdb.OperationalError
IntegrityError = MySQLdb.IntegrityError

def connect(cfg):
	return MySQLdb.connect(
		host = cfg.get('host', 'localhost'),
		db = cfg.get('name', 'rosshmdb'),
		user = cfg.get('user', 'rosshm'),
		passwd = cfg.get('password', None),
	)
