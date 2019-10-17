# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.core.view import status

def test_view(testing_wapp):
	with testing_wapp('core', db = True) as ctx:
		d = status.view(ctx.db)
		assert isinstance(d, dict)
		assert d['status'] == 'ok'

def test_no_status(testing_wapp):
	with testing_wapp('core', db = True) as ctx:
		_pk = status._pk
		try:
			status._pk = 9
			d = status.view(ctx.db)
			assert isinstance(d, dict)
			assert d == {}
		finally:
			status._pk = _pk
