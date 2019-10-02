# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log
from rosshm.db.schema.status import DBStatus

def view(db):
	log.debug('view')
	s = DBStatus()
	row = s.get(db, 'status', pk = 0)
	if row is None:
		return {}
	return dict(row)
