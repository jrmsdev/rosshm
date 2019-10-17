# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.wapp.plugin.db import DBPlugin
from rosshm.db.conn import DBConn

def _new(ctx):
	debug = ctx.wapp.config.getbool('debug')
	dbcfg = ctx.wapp.config.database()
	return DBPlugin(dbcfg, debug)

def test_setup(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		p.setup(ctx.wapp.wapp)

def _callback(db, *args, **kwargs):
	tdata = kwargs.get('tdata', None)
	return {'db': db, 'tdata': tdata}

def test_apply(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		del ctx.callback
		ctx.callback = _callback
		d = p.apply(ctx.callback, ctx.route)(tdata = 'testing')
		assert isinstance(d, dict)
		assert d['tdata'] == 'testing'
		assert isinstance(d['db'], DBConn)
