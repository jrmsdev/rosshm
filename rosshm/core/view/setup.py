# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from rosshm import log, config
from rosshm.db import db

def redirect(rpath = ''):
	"""redirect all non setup requests"""
	log.debug('redir')
	bottle.redirect('/_/setup')

def _dbconn():
	"""get database connection"""
	dbcfg = config.database()
	log.debug(f"dbcfg {dbcfg['driver']} {dbcfg['name']}")
	return db.connect(dbcfg)

def _dbstatus():
	"""get database status table info"""
	log.debug('db status')
	status = {}
	error = None
	try:
		conn = _dbconn()
		status = db.status(conn)
		conn.close()
		if status is not None:
			status = dict(status)
	except db.DatabaseError as err:
		log.error(f"check database: {err}")
		error = str(err)
	return {'error': error, 'status': status, 'db': config.database()}

@bottle.view('core/setup/index.html')
def index():
	"""index view"""
	log.debug('view')
	return _dbstatus()

@bottle.view('core/setup/db/create.html')
def dbCreate():
	"""create database"""
	log.debug('db create')
	dbstat = _dbstatus()
	if dbstat['error'] is None:
		# database is ok?
		return {'error': 'database already created?', 'db': config.database()}
	rv = {}
	req = bottle.request
	if req.method == 'POST':
		log.debug('db create action')
		try:
			conn = _dbconn()
			rv = db.create(conn)
			conn.close()
			bottle.redirect('/_/setup')
		except db.DatabaseError as err:
			log.error(f"create database: {err}")
			rv['error'] = str(err)
		except db.IntegrityError as err:
			log.error(f"create database: {err}")
			rv['error'] = str(err)
			log.debug('rollback')
			conn.rollback()
	rv['db'] = config.database()
	return rv
