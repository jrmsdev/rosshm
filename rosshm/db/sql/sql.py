# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

from rosshm import log
from rosshm.db.sql import insert as mod_insert
from rosshm.db.sql import select as mod_select
from rosshm.db.sql import table

__all__ = ['setLang', 'createTable', 'insert', 'select']

# lang specifics manager
lang = None

def setLang(manager):
	global lang
	log.debug(f"set lang {manager.name}")
	lang = manager
	table.lang = manager
	mod_insert.lang = manager
	mod_select.lang = manager

createTable = table.create
insert = mod_insert.insert
select = mod_select.select
