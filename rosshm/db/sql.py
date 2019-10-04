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
	elif typ is int:
		f += " INT"
	if not args.get('null', False):
		f += " NOT NULL"
	return f

def _mkStr(args):
	size = args.get('size', 0)
	if size > 0:
		return "VARCHAR(%d)" % size
	return 'TEXT'

#
# INSERT
#
def insert(obj, data):
	table = obj.table
	fields = tuple(obj.fields.keys())
	fl = deque()
	vl = deque()
	for k, v in data.items():
		if k == 'pk' or k in fields:
			fl.append(k)
			vl.append(v)
	s = "INSERT INTO rosshm_%s" % table
	s += " (%s)" % ', '.join(fl)
	s += " VALUES (%s);" % ', '.join(['?' for x in vl])
	log.debug(s)
	return (s, vl)

#
# SELECT
#
def select(obj, filter, where):
	table = obj.table
	fields = tuple(obj.fields.keys())
	args = tuple()
	select = '*'
	flen = len(filter)
	if flen == 1:
		select = filter[0]
	elif flen > 1:
		names = deque()
		for n in filter:
			if n in fields:
				names.append(n)
		select = "%s" % ', '.join(names)
	s = "SELECT %s FROM rosshm_%s" % (select, table)
	for k, v in where.items():
		if k == 'pk' or k in fields:
			s += " WHERE %s=?" % k
			args += (v,)
	s += ";"
	log.debug(s)
	return (s, args)
