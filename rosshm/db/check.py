# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs

from rosshm import log
from rosshm.db import db

__all__ = ['checkdb']

def checkdb(config, conn = None):
	dbcfg = config.database()
	log.debug(f"checkdb {dbcfg['driver']} {dbcfg['name']} {dbcfg['config']}")
	if dbcfg.get('driver') == 'sqlite' and dbcfg.get('name') != ':memory:':
		dbfn = dbcfg.get('name')
		if not path.isfile(dbfn):
			makedirs(path.dirname(dbfn), mode = 0o750, exist_ok = True)
	rv = True
	try:
		if conn is None:
			conn = db.connect(dbcfg)
		rv = _check(conn)
	except db.DatabaseError as err:
		log.error(f"check database: {err}")
		return False
	finally:
		if conn is not None:
			conn.close()
	return rv

def _check(conn):
	log.debug('db status')
	s = db.status(conn)
	if not s:
		return False
	return s['status'] == 'ok'
