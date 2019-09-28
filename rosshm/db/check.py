# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs

from rosshm import log
from rosshm.db import db

__all__ = ['checkdb']

def checkdb(config):
	log.debug('checkdb')
	dbfn = path.abspath(path.join(config.get('datadir'), 'rosshm.db'))
	log.debug(f"dbfn {dbfn}")
	if not path.isfile(dbfn):
		makedirs(path.dirname(dbfn), mode = 0o750, exist_ok = True)
	rv = True
	try:
		conn = db.connect(dbfn)
		rv = _check(conn)
	except db.Error as err:
		log.error(f"check database: {err}")
		return False
	return rv

def _check(conn):
	log.debug('db status')
	s = db.status(conn)
	conn.close()
	if not s:
		return False
	return s.get('status', 'none') == 'ok'
