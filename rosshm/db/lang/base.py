# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class LangBase(object):
	name = None
	fmt = '?'

	def primaryKey(self, name = 'pk'):
		return f"{name} INTEGER PRIMARY KEY AUTOINCREMENT"

	def valfmt(self, typ):
		return f"{self.fmt}"

	def tableOptions(self):
		return ''
