# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from rosshm import log
from rosshm.db.sql import sql
from rosshm.db.lang.sqlite import SqliteLang

DatabaseError = sqlite3.DatabaseError
IntegrityError = sqlite3.IntegrityError

def connect(cfg):
	log.debug('connect')
	sql.setLang(SqliteLang())
	name = cfg.get('name')
	if name.startswith(':memory:'):
		memdb = name.split(':')[2].strip()
		if memdb == '':
			memdb = 'rosshmdb'
		uri = f"file:{memdb}?mode=memory&cache=shared"
	else:
		uri = f"file:{name}?cache=shared"
	log.debug(f"uri {uri}")
	conn = sqlite3.connect(uri, uri = True)
	conn.row_factory = sqlite3.Row
	return conn
