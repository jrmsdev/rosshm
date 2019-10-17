# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.wapp.plugin.db import DBPlugin

def test_setup(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		debug = ctx.wapp.config.getbool('debug')
		dbcfg = ctx.wapp.config.database()
		p = DBPlugin(dbcfg, debug)
		p.setup(ctx.wapp.wapp)
