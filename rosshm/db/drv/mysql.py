# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import MySQLdb

from rosshm import log
from rosshm.db.conn import DBConn

Error = MySQLdb.OperationalError
IntegrityError = MySQLdb.IntegrityError

def connect(cfg):
	log.debug(f"connect paramstyle='{MySQLdb.paramstyle}'")
	return DBConn(MySQLdb.connect(
		host = cfg.get('host', 'localhost'),
		db = cfg.get('name', 'rosshmdb'),
		user = cfg.get('user', 'rosshm'),
		passwd = cfg.get('password', None),
	))
