# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from contextlib import contextmanager
from unittest.mock import Mock

from rosshm.static import static

_rootdir = static._rootdir
_static_file = static.bottle.static_file

@contextmanager
def static_ctx():
	try:
		static.bottle.static_file = Mock(return_value = True)
		static._rootdir = '/opt/src/rosshm/static'
		yield static
	finally:
		del static._rootdir
		static._rootdir = _rootdir
		del static.bottle.static_file
		static.bottle.static_file = _static_file

def test_extensions():
	with static_ctx() as ctx:
		assert sorted(ctx._serveExtension.keys()) == ['.css']

def test_notfound():
	with static_ctx() as ctx:
		resp = ctx.serve('testing.txt')
		assert isinstance(resp, bottle.HTTPError)
		assert resp.status_code == 404

def test_serve():
	with static_ctx() as ctx:
		assert ctx.serve('default.css')
		ctx.bottle.static_file.assert_called_once_with('default.css', root = ctx._rootdir)
