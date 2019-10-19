# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from collections import namedtuple
from os import path

from rosshm import log, config
from rosshm.db import db

__all__ = ['redirect', 'index', 'dbCreate']

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
def dbCreate(req = None):
	"""create database"""
	log.debug('db create')
	dbstat = _dbstatus()
	if dbstat['error'] is None:
		# database is ok?
		return {'error': 'database already created?', 'db': config.database()}
	if req is None:
		req = bottle.request
	rv = {}
	if req.method == 'POST':
		log.debug('db create action')
		admin = _getAdmin(req)
		conn = None
		try:
			conn = _dbconn()
			log.info(f"create admin user: {admin.username}")
			rv = db.create(conn, admin)
			conn.commit()
			bottle.redirect('/_/setup')
		except db.IntegrityError as err:
			log.error(f"create database integrity error: {err}")
			rv['error'] = str(err)
			if conn is not None:
				log.debug('rollback')
				conn.rollback()
		except db.DatabaseError as err:
			log.error(f"create database: {err}")
			rv['error'] = str(err)
			if conn is not None:
				log.debug('rollback')
				conn.rollback()
		finally:
			if conn is not None:
				conn.close()
	rv['db'] = config.database()
	return rv

_Admin = namedtuple('Admin', ['username', 'password'])

def _getAdmin(req):
	"""return admin username and password from request forms data as namedtuple"""
	username = req.forms.admin_user,
	password = req.forms.admin_password,
	errors = []
	if username[0] == '':
		errors.append('admin username is empty')
	if password[0] == '':
		errors.append('admin password is empty')
	if errors:
		for err in errors:
			log.error(err)
		raise bottle.HTTPError(400, '\n'.join(errors))
	return _Admin(username = username[0], password = password[0])
