# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from rosshm import log
from rosshm.db import db

def redirect(rpath = ''):
	log.debug('redir')
	bottle.redirect('/_/setup')

@bottle.view('core/setup/index.html')
def view():
	log.debug('view')
	try:
		conn = db.connect(dbfn)
		status = db.status(conn)
		conn.close()
	except db.Error as err:
		log.error(f"check database: {err}")
		status = {'error': str(err)}
	return {'status': status}
