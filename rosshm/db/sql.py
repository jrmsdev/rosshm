# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

from rosshm import log

#
# CREATE TABLE
#
def createTable(name, fields):
	s = "CREATE TABLE rosshm_%s" % name
	fl = deque()
	fl.append('pk INTEGER PRIMARY KEY AUTOINCREMENT')
	for f, d in fields.items():
		typ = d[0]
		args = d[1]
		fl.append(_mkfield(f, typ, args))
	s += " (%s);" % ', '.join(fl)
	log.debug(s)
	return s

def _mkfield(name, typ, args):
	f = name
	if typ is str:
		f += " %s" % _mkStr(args)
	return f

def _mkStr(args):
	size = args.get('size', 0)
	if size > 0:
		return "VARCHAR(%d)" % size
	return 'TEXT'

#
# SELECT
#
def select(table, fields, where, filter):
	fields = tuple(fields)
	args = tuple()
	select = '*'
	if len(filter) > 0:
		names = []
		for n in filter:
			if n in fields:
				names.append(n)
		select = "(%s)" % ', '.join(names)
	s = "SELECT %s FROM rosshm_%s" % (select, table)
	for k, v in where.items():
		if k in fields:
			s += " WHERE %s=?" % k
			args += (v,)
	s += ";"
	log.debug(s)
	return (s, args)
