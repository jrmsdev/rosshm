# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

from rosshm import log

# lang specifics manager
lang = None

def setLang(manager):
	global lang
	log.debug(f"set lang {manager.name}")
	lang = manager

# get fields type
def fieldType(fields, name):
	if name == 'pk':
		return int
	m = fields.get(name)
	return m[0]

#
# CREATE TABLE
#
def createTable(name, fields):
	s = f"CREATE TABLE rosshm_{name}"
	fl = deque()
	fl.append(lang.primaryKey())
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
	vfmt = deque()
	for k, v in data.items():
		if k == 'pk' or k in fields:
			fl.append(k)
			vl.append(v)
			typ = fieldType(obj.fields, k)
			vfmt.append(lang.valfmt(typ))
	s = f"INSERT INTO rosshm_{table}"
	s += " (%s)" % ', '.join(fl)
	s += " VALUES (%s);" % ', '.join(vfmt)
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
	s = f"SELECT {select} FROM rosshm_{table} WHERE"
	i = 0
	cond = ' AND '
	for k, v in where.items():
		if i == 0:
			cond = ' '
		if k == 'pk' or k in fields:
			typ = fieldType(obj.fields, k)
			s += f"{cond}{k}=" + lang.valfmt(typ)
			args += (v,)
		i += 1
	s += ";"
	log.debug(s)
	return (s, args)
