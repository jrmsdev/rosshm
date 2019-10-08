# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

from rosshm import log

lang = None

def create(name, fields):
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
