# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from rosshm import log, config
from rosshm.db import db

def redirect(rpath = ''):
	log.debug('redir')
	bottle.redirect('/_/setup')

def _dbstatus():
	dbfn = path.abspath(path.join(config.get('datadir'), 'rosshm.db'))
	log.debug(f"dbfn {dbfn}")
	status = {}
	error = None
	try:
		conn = db.connect(dbfn)
		status = db.status(conn)
		conn.close()
	except db.Error as err:
		log.error(f"check database: {err}")
		error = str(err)
	return {'error': error, 'status': status}

@bottle.view('core/setup/index.html')
def index():
	log.debug('view')
	return _dbstatus()

@bottle.view('core/setup/db/create.html')
def dbCreate():
	log.debug('db create')
	dbstat = _dbstatus()
	if dbstat['error'] is None:
		# database is ok?
		return {'error': 'database already created?'}
	return {}
