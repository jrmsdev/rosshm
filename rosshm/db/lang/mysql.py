# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.lang.base import LangBase

class MySQLLang(LangBase):
	name = 'mysql'
	paramstyle = None # set at connect time
