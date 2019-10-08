# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

from rosshm import log
from rosshm.db.utils import fieldType

lang = None

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
			args += (typ(v),)
		i += 1
	s += ";"
	log.debug(s)
	return (s, args)
