# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from rosshm.wapp.plugin.response import Plugin

def _new(ctx, debug = False):
	return Plugin(debug)

def test_setup(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		p.setup(ctx.wapp.wapp)
		assert p.name == 'rosshm.response'
		assert p.api == 2

def _callback():
	return bottle.HTTPResponse(status = 200, body = 'testing')

def test_apply_http_response(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		ctx.callback.side_effect = _callback
		resp = p.apply(ctx.callback, ctx.route)()
		assert isinstance(resp, bottle.HTTPResponse)
		assert resp.status_code == 200
		assert resp.body == 'testing'

def test_apply(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		resp = p.apply(ctx.callback, ctx.route)('testing')
		assert isinstance(resp, dict)
		assert resp == {'tdata': 'testing'}

def test_apply_debug(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx, debug = True)
		resp = p.apply(ctx.callback, ctx.route)('testing')
		assert isinstance(resp, dict)
		assert resp == {'tdata': 'testing'}
