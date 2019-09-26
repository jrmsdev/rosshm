# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log

def view(db):
	log.debug('view')
	return {'status': 'ok'}
