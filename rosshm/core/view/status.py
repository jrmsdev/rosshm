# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log
from rosshm.core.db.schema.status import DBStatus

_pk = 1

def view(db):
	"""show core status info"""
	log.debug('view')
	s = DBStatus()
	row = s.get(db, 'status', pk = _pk)
	if row is None:
		return {}
	return dict(row)
