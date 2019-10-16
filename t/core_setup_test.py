# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.core.view import setup

def test_redirect(testing_wapp):
	with testing_wapp('core') as ctx:
		setup.redirect()
		ctx.redirect.assert_called_with('/_/setup')
