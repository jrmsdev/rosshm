# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs

from rosshm import log
from rosshm.db import db

def checkdb(fn):
	log.debug(f"checkdb {fn}")
	if not path.isfile(fn):
		makedirs(path.dirname(fn), mode = 0o750, exist_ok = True)
	if not db.check(fn):
		return False
	return True
