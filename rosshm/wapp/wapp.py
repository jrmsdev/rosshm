# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from rosshm import config, log, version
from rosshm.core import core
from rosshm.web import web

__all__ = ['init']

def init():
	config.init()
	debug = config.getbool('debug')

	if debug:
		log.init('debug')
	else:
		log.init(config.get('log.level'))
	log.debug(f"rosshm version {version.get()}")

	bottle.TEMPLATE_PATH = []
	wapp = bottle.Bottle()
	log.debug('bottle config')
	wapp.config.load_config(config.filename())

	if config.getbool('core.enable'):
		log.debug('core init')
		core.init(config, wapp)

	if config.getbool('web.enable'):
		log.debug('web init')
		web.init(config, wapp)

	return wapp
