# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from rosshm.core.view import setup

def test_redirect(testing_wapp):
	with testing_wapp('core') as ctx:
		setup.redirect()
		bottle.redirect.assert_called_with('/_/setup')

def test_index(testing_wapp):
	with testing_wapp('core') as ctx:
		d = setup.index()
		# ~ assert isinstance(d, dict)
		bottle.view.assert_any_call('core/setup/db/create.html')
