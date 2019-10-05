# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class LangBase(object):
	name = None
	paramstyle = 'qmark'

	def primaryKey(self, name = 'pk'):
		return f"{name} INTEGER PRIMARY KEY AUTOINCREMENT"

	def valfmt(self, typ):
		if self.paramstyle == 'format':
			return self._format(typ)
		return self._qmark(typ)

	def _qmark(self, typ):
		return '?'

	def _format(self, typ):
		if typ is int:
			return '%s'
		return "'%s'"
