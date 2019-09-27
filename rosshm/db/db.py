# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

def connect(fn):
	return sqlite3.connect(fn)
