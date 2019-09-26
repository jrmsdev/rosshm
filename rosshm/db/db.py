# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

def check(fn):
	conn = sqlite3.connect(fn)
	conn.close()
	return True
