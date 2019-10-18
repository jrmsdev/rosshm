# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db import db
from rosshm.db.lang.mysql import MySQLLang
from rosshm.db.sql import sql

import MySQLdb # from tlib

def test_connect(testing_config):
	with testing_config('mysql.ini') as config:
		conn = None
		dbcfg = config.database()
		assert dbcfg == {
			'config': '',
			'driver': 'mysql',
			'name': 'rosshmdb',
		}
		try:
			conn = db.connect(dbcfg)
		finally:
			if conn:
				conn.close()
		assert db.DatabaseError == MySQLdb.DatabaseError
		assert db.IntegrityError == MySQLdb.IntegrityError
		assert sql.lang.name == 'mysql'
		MySQLdb.connect.assert_called_once_with(
			charset='utf8',
			connect_timeout=60,
			cursorclass='TestingDictCursor',
			db='rosshmdb',
			host='localhost',
			passwd=None,
			use_unicode=True,
			user='rosshm',
		)

def test_lang():
	l = MySQLLang()
	assert l.name == 'mysql'
	assert l.fmt == '%s'
	assert l.tableOptions() == 'CHARACTER SET utf8 COLLATE utf8_bin'
	assert l.primaryKey() == 'pk INT PRIMARY KEY AUTO_INCREMENT'
	assert l.valfmt(str) == '%s'
	assert l.valfmt(int) == '%s'
	assert l.valfmt(bool) == '%s'
