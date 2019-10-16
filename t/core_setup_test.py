# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from rosshm.core.view import setup

def test_redirect(testing_wapp):
	with testing_wapp('core') as ctx:
		setup.redirect()
		bottle.redirect.assert_called_with('/_/setup')

def test_index(testing_wapp):
	with testing_wapp('core', db = True) as ctx:
		d = setup.index()
		bottle.view.assert_any_call('core/setup/index.html')
		assert isinstance(d, dict)
		assert d == {
			'db': {
				'config': '',
				'driver': 'sqlite',
				'name': ':memory:',
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
