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
	fn = cfg.get('name')
	conn = sqlite3.connect(f"file:{fn}?cache=shared", uri = True)
	conn.row_factory = sqlite3.Row
	return conn
