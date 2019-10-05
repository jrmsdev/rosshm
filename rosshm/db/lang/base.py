# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class BaseLang(object):
	name = None

	def primaryKey(self, name = 'pk'):
		return f"{name} INTEGER PRIMARY KEY AUTOINCREMENT"

	def valfmt(self, typ):
		if typ is str:
			return "'?'"
		return '?'
