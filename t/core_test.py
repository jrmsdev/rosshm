# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.core import core
from rosshm.core.view import setup, status

def test_init_setup(testing_wapp):
	with testing_wapp('core') as ctx:
		ctx.wapp.route.assert_any_call('/', 'GET',
			setup.redirect, name = 'setup.redir')
		ctx.wapp.route.assert_any_call('/_/setup', 'GET',
			setup.index, name = 'setup')
		ctx.wapp.route.assert_any_call('/_/setup/db/create', ['GET', 'POST'],
			setup.dbCreate, name = 'db.create')
		ctx.wapp.route.assert_any_call('/<rpath:path>', 'GET',
			setup.redirect, name = 'setup.redirall')

def test_init_views(testing_wapp):
	with testing_wapp('core', db = True) as ctx:
		ctx.wapp.route.assert_any_call('/_/', 'GET', status.view,
			apply = core._plugins, name = 'core.status')
