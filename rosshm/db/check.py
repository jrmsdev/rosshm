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
	try:
		conn = db.connect(dbfn)
		conn.close()
	except Exception as err:
		log.error(str(err))
		return False
	return _check(conn)

def _check(db):
	return False
