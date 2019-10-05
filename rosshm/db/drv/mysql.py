# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import MySQLdb
from MySQLdb.cursors import DictCursor

from rosshm import log
from rosshm.db import sql
from rosshm.db.lang.mysql import MySQLLang

DatabaseError = MySQLdb.DatabaseError
IntegrityError = MySQLdb.IntegrityError

def connect(cfg):
	log.debug('connect')
	lang = MySQLLang()
	lang.paramstyle = MySQLdb.paramstyle
	sql.setLang(lang)
	return MySQLdb.connect(
		host            = cfg.get('host'    , 'localhost'),
		db              = cfg.get('name'    , 'rosshmdb'),
		user            = cfg.get('user'    , 'rosshm'),
		passwd          = cfg.get('password', None),
		connect_timeout = cfg.get('timeout' , 60),
		charset         = cfg.get('charset' , 'utf8'),
		use_unicode     = True,
		cursorclass     = DictCursor,
	)
