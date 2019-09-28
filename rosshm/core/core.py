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
	if checkdb(config):
		_views(config, wapp)
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

def _views(config, wapp):
	log.debug('init views')
	log.debug('sqlite plugin')
	dbfn = path.abspath(path.join(config.get('datadir'), 'rosshm.db'))
	dbplugin = sqlite.Plugin(dbfile = dbfn)
	wapp.route('/_/', 'GET', status.view, name = 'core.status',
		apply = [dbplugin])
