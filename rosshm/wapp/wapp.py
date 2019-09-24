# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import Bottle

from rosshm import config, log, version

__all__ = ['init']

def init():
	config.init()
	debug = config.getbool('debug')
	if debug:
		log.init('debug')
	else:
		log.init(config.get('log.level'))
	log.debug(f"rosshm version {version.get()}")
	wapp = Bottle()
	if config.getbool('core.enable'):
		log.debug('core enable')
	if config.getbool('web.enable'):
		log.debug('web enable')
	return wapp
