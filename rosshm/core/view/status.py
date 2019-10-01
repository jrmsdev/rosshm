# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log
from rosshm.db.obj.status import DBStatus

def view(db):
	log.debug('view')
	s = DBStatus()
	return s.get(db, 'status', pk = 0)
