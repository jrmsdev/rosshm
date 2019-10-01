# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from rosshm import log, config
from rosshm.db import db

#
# redirect all non setup requests
#
def redirect(rpath = ''):
	log.debug('redir')
	bottle.redirect('/_/setup')

#
# get database connection
#
def _dbconn():
	dbcfg = config.database()
	log.debug(f"dbcfg {dbcfg}")
	return db.connect(dbcfg)

#
# get database status table info
#
def _dbstatus():
	log.debug('db status')
	status = {}
	error = None
	try:
		conn = _dbconn()
		status = db.status(conn)
		conn.close()
	except db.Error as err:
		log.error(f"check database: {err}")
		error = str(err)
	return {'error': error, 'status': status, 'db': config.database()}

#
# index view
#
@bottle.view('core/setup/index.html')
def index():
	log.debug('view')
	return _dbstatus()

#
# create database
#
@bottle.view('core/setup/db/create.html')
def dbCreate():
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
		except db.Error as err:
			log.error(f"create database: {err}")
			rv['error'] = str(err)
	rv['db'] = config.database()
	return rv
