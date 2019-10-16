# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from rosshm.libdir import libdir
from rosshm.static import static

_bottle_ini = path.abspath(libdir / 'wapp' / 'bottle.ini')

def test_init(testing_wapp):
	with testing_wapp('wapp') as ctx:
		ctx.config.init.assert_called_once_with(fn = None)
		ctx.Bottle.assert_called_once_with()
		ctx.wapp.config.load_config.assert_called_once_with(_bottle_ini)
		ctx.wapp.install.assert_called_once()
		ctx.wapp.route.assert_called_once_with('/static/<filename:re:.*\\..*>',
			'GET', static.serve, name = 'static')
