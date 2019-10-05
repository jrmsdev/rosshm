# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.lang.base import LangBase

class MySQLLang(LangBase):
	name = 'mysql'
	fmt = '%s'

	def primaryKey(self, name = 'pk'):
		return f"{name} INT PRIMARY KEY AUTO_INCREMENT"
