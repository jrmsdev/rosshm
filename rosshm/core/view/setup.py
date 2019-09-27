# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from rosshm import log

def redirect(rpath = ''):
	log.debug('redir')
	bottle.redirect('/_/setup')

@bottle.view('core/setup/index.html')
def view():
	log.debug('view')
	return {}
