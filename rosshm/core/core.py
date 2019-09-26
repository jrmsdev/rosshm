# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle.ext import sqlite
from os import path

from rosshm import log
from rosshm.core.view import status

__all__ = ['init']

def init(config, wapp):
	log.debug(f"init {config.filename()}")

	dbfn = path.abspath(path.join(config.get('datadir'), 'rosshm.db'))
	log.debug(f"dbfn {dbfn}")

	log.debug('sqlite plugin')
	dbplugin = sqlite.Plugin(dbfile = dbfn)

	# ~ wapp.install(dbplugin)

	wapp.route('/_/', 'GET', status.view, name = 'core.status',
		apply = [dbplugin])
