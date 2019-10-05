# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

Error = sqlite3.OperationalError
IntegrityError = sqlite3.IntegrityError

def connect(cfg):
	fn = cfg.get('name')
	conn = sqlite3.connect(f"file:{fn}?cache=shared", uri = True)
	conn.row_factory = sqlite3.Row
	return conn
