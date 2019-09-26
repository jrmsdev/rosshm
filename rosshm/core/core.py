# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle.ext import sqlite
from os import path

from rosshm import log
from rosshm.core.view import setup, status
from rosshm.db.check import checkdb

__all__ = ['init']

def init(config, wapp):
	log.debug(f"init {config.filename()}")

	dbfn = path.abspath(path.join(config.get('datadir'), 'rosshm.db'))
	log.debug(f"dbfn {dbfn}")

	if checkdb(dbfn):
		_views(config, wapp, dbfn)
		return True
	else:
		_setup(config, wapp)
		return False

def _setup(config, wapp):
	log.debug('setup')
	wapp.route('/', 'GET', setup.redirect, name = 'setup.redir')
	wapp.route('/_/setup', 'GET', setup.view, name = 'setup')
	wapp.route('/<rpath:path>', 'GET', setup.redirect, name = 'setup.redirall')

def _views(config, wapp, dbfn):
	log.debug('views')
	log.debug('sqlite plugin')
	dbplugin = sqlite.Plugin(dbfile = dbfn)
	wapp.route('/_/', 'GET', status.view, name = 'core.status',
		apply = [dbplugin])
