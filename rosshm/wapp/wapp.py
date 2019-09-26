# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from rosshm import config, log, version
from rosshm.core import core
from rosshm.libdir import libdir
from rosshm.wapp.plugin import response
from rosshm.web import web

__all__ = ['init']

def init(cfgfn = None):
	config.init(fn = cfgfn)

	debug = config.getbool('debug')
	if debug:
		log.init('debug')
	else:
		log.init(config.get('log.level'))
	log.debug(f"rosshm version {version.get()}")

	tpldir = path.abspath(libdir / 'web' / 'tpl')
	log.debug(f"templates path {tpldir}")
	bottle.TEMPLATE_PATH = []

	wapp = bottle.Bottle()

	for inifn in (path.abspath(libdir / 'wapp' / 'bottle.ini'), config.get('wapp.ini')):
		if inifn == '': continue
		log.debug(f"bottle config {inifn}")
		wapp.config.load_config(inifn)

	log.debug('install plugins')
	wapp.install(response.Plugin(debug = debug))

	coreok = False
	if config.getbool('core.enable'):
		log.debug('core init')
		coreok = core.init(config, wapp)

	log.debug(f"coreok {coreok}")
	if coreok and config.getbool('web.enable'):
		log.debug('web init')
		web.init(config, wapp)

	return wapp
