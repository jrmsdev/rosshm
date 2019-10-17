# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager

from testing.wapp_ctx import wapp_ctx

class WappPluginCtx(object):
	wapp = None

	def __init__(self, wapp):
		self.wapp = wapp

@contextmanager
def wapp_plugin_ctx():
	with wapp_ctx('plugin') as wapp:
		ctx = WappPluginCtx(wapp)
		yield ctx
