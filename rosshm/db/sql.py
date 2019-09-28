# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log

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
