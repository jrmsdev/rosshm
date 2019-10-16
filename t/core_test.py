# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import call

from rosshm.core import core
from rosshm.core.view import setup, status

def test_init_setup(testing_wapp):
	with testing_wapp('core') as ctx:
		assert ctx.wapp.route.mock_calls == [
			call('/', 'GET', setup.redirect, name = 'setup.redir'),
			call('/_/setup', 'GET', setup.index, name = 'setup'),
			call('/_/setup/db/create', ['GET', 'POST'], setup.dbCreate, name = 'db.create'),
			call('/<rpath:path>', 'GET', setup.redirect, name = 'setup.redirall'),
		]

def test_init_views(testing_wapp):
	with testing_wapp('core', db = True) as ctx:
		assert ctx.wapp.route.mock_calls == [
			call('/_/', 'GET', status.view, apply = core._plugins, name = 'core.status'),
		]
