# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class LangBase(object):
	name = None
	paramstyle = 'qmark'

	def primaryKey(self, name = 'pk'):
		return f"{name} INTEGER PRIMARY KEY AUTOINCREMENT"

	def valfmt(self, typ):
		if self.paramstyle == 'qmark':
			return self._qmark(typ)

	def _qmark(self, typ):
		return '?'
