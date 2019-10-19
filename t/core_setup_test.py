# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from unittest.mock import Mock

from rosshm.core.view import setup
from rosshm.db import db

def test_redirect(testing_wapp):
	with testing_wapp('core') as ctx:
		with ctx.redirect('/_/setup'):
			setup.redirect()

def test_index(testing_wapp):
	with testing_wapp('core', db = True) as ctx:
		d = setup.index()
		bottle.view.assert_any_call('core/setup/index.html')
		assert isinstance(d, dict)
		assert d == {
			'db': {
				'config': '',
				'driver': 'sqlite',
				'name': ':memory:core_testdb',
			},
			'error': None,
			'status': {'status': 'ok'},
		}

def test_no_status(testing_wapp):
	with testing_wapp('core') as ctx:
		d = setup.index()
		assert isinstance(d, dict)
		err = d['error']
		assert err == 'no such table: rosshm_status'

def test_db_create(testing_wapp):
	with testing_wapp('core') as ctx:
		d = setup.dbCreate()
		assert isinstance(d, dict)
		assert d == {'db': {'config': '', 'driver': 'sqlite', 'name': ':memory:core_testdb'}}

def test_db_create_POST(testing_wapp):
	with testing_wapp('core') as ctx:
		req = ctx.request(post = {'admin_user': 'admin', 'admin_password': 'testing'})
		with ctx.redirect('/_/setup'):
			setup.dbCreate(req = req)

def test_db_is_created(testing_wapp):
	with testing_wapp('core', db = True) as ctx:
		d = setup.dbCreate()
		assert isinstance(d, dict)
		err = d['error']
		assert err == 'database already created?'

def test_db_integrity_error(testing_wapp):
	with testing_wapp('core') as ctx:
		req = ctx.request(post = {'admin_user': 'admin', 'admin_password': 'testing'})
		db_create = setup.db.create
		try:
			setup.db.create = Mock()
			setup.db.create.side_effect = db.IntegrityError('testing integrity error')
			d = setup.dbCreate(req = req)
			err = d['error']
			assert err == 'testing integrity error'
		finally:
			del setup.db.create
			setup.db.create = db_create

def test_database_error(testing_wapp):
	with testing_wapp('core', db = True) as ctx:
		req = ctx.request(post = {'admin_user': 'admin', 'admin_password': 'testing'})
		_dbconn = setup._dbconn
		try:
			setup._dbconn = Mock()
			setup._dbconn.side_effect = db.DatabaseError('testing db error')
			d = setup.dbCreate(req = req)
			err = d['error']
			assert err == 'testing db error'
		finally:
			del setup._dbconn
			setup._dbconn = _dbconn
