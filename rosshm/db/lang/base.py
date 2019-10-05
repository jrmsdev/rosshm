# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class BaseLang(object):

	def createTable(self, name):
		return f"CREATE TABLE rosshm_{name}"

	def primaryKey(self, name = 'pk'):
		return f"{name} INTEGER PRIMARY KEY AUTOINCREMENT"
