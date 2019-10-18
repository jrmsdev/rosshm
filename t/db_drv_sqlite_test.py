# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import makedirs, path
from shutil import rmtree

from rosshm.db import db
from rosshm.db.drv import sqlite
from rosshm.db.lang.sqlite import SqliteLang
from rosshm.db.sql import sql

_dbdir = path.join('tdata', 'var', 'sqlite')
_dbfn = path.join(_dbdir, 'rosshm.sqlite')

def test_connect(testing_db):
	try:
		makedirs(_dbdir, mode = 0o0700, exist_ok = True)
		with testing_db('sqlite.ini') as conn:
			assert db.DatabaseError == sqlite.DatabaseError
			assert db.IntegrityError == sqlite.IntegrityError
			assert sql.lang.name == 'sqlite'
	finally:
		rmtree(_dbdir)

def test_lang():
	l = SqliteLang()
	assert l.name == 'sqlite'
	assert l.fmt == '?'
	assert l.tableOptions() == ''
	assert l.primaryKey() == 'pk INTEGER PRIMARY KEY AUTOINCREMENT'
	assert l.valfmt(str) == '?'
	assert l.valfmt(int) == '?'
	assert l.valfmt(bool) == '?'
