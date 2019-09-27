# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

__all__ = ['connect', 'status']

def connect(fn):
	return sqlite3.connect(fn)

def status(db):
	return {'status': 'initdb'}
