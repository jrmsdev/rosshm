# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from rosshm import log
from rosshm.core.view import setup, status
from rosshm.db.check import checkdb
from rosshm.wapp.plugin.db import DBPlugin

__all__ = ['init']

def init(config, wapp):
	log.debug(f"init {config.filename()}")
	debug = config.getbool('debug')
	if checkdb(config):
		log.debug('sqlite plugin')
		dbfn = path.abspath(path.join(config.get('datadir'), 'rosshm.db'))
		plugins = [DBPlugin(dbfn, debug = debug)]
		_views(config, wapp, plugins)
		return True
	else:
		_setup(config, wapp)
		return False

def _setup(config, wapp):
	log.debug('init setup')
	wapp.route('/', 'GET', setup.redirect, name = 'setup.redir')
	wapp.route('/_/setup', 'GET', setup.index, name = 'setup')
	wapp.route('/_/setup/db/create', ['GET', 'POST'],
		setup.dbCreate, name = 'db.create')
	wapp.route('/<rpath:path>', 'GET', setup.redirect, name = 'setup.redirall')

def _views(config, wapp, plugins):
	log.debug('init views')
	wapp.route('/_/', 'GET', status.view, name = 'core.status',
		apply = plugins)
