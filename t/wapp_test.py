# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from rosshm.libdir import libdir
from rosshm.static import static

_bottle_ini = path.abspath(libdir / 'wapp' / 'bottle.ini')

def test_init(testing_wapp):
	with testing_wapp('wapp') as ctx:
		ctx.config.init.assert_called_once_with(fn = None)
		bottle.Bottle.assert_any_call()
		ctx.wapp.config.load_config.assert_any_call(_bottle_ini)
		ctx.wapp.install.assert_called()
		ctx.wapp.route.assert_any_call('/static/<filename:re:.*\\..*>',
			'GET', static.serve, name = 'static')
