# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.wapp.plugin.response import Plugin

def _new(ctx):
	debug = ctx.wapp.config.getbool('debug')
	return Plugin(debug)

def test_setup(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		p.setup(ctx.wapp.wapp)
		assert p.name == 'rosshm.response'
		assert p.api == 2
