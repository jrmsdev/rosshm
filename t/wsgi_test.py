# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

import rosshm.wapp.wapp

def test_application():
	init = rosshm.wapp.wapp.init
	rosshm.wapp.wapp.init = Mock(return_value = 'init_done')
	try:
		from rosshm import wsgi
		assert wsgi.application == 'init_done'
	finally:
		del rosshm.wapp.wapp.init
		rosshm.wapp.wapp.init = init
