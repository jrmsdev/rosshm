# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock

from testing.wapp_ctx import wapp_ctx

class WappPluginCtx(object):
	wapp = None
	callback = None
	route = None

	def __init__(self, wapp):
		self.wapp = wapp
		self.callback = Mock()
		self.callback.side_effect = lambda x: {'tdata': x}
		self.route = Mock()
		self.route.name = 'testing'

@contextmanager
def wapp_plugin_ctx():
	with wapp_ctx('plugin') as wapp:
		ctx = WappPluginCtx(wapp)
		yield ctx
