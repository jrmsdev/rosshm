# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import Bottle

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
	wapp = Bottle()
	log.debug('bottle config')
	wapp.config.load_config(config.filename())
	if config.getbool('core.enable'):
		log.debug('core init')
		core.init(config)
	if config.getbool('web.enable'):
		log.debug('web init')
		web.init(config)
	return wapp
