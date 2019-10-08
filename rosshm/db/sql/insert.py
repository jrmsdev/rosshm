# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

from rosshm import log
from rosshm.db.utils import fieldType

lang = None

def insert(obj, data):
	table = obj.table
	fields = tuple(obj.fields.keys())
	fl = deque()
	vl = deque()
	vfmt = deque()
	for k, v in data.items():
		if k == 'pk' or k in fields:
			fl.append(k)
			typ = fieldType(obj.fields, k)
			vfmt.append(lang.valfmt(typ))
			vl.append(typ(v))
	s = f"INSERT INTO rosshm_{table}"
	s += " (%s)" % ', '.join(fl)
	s += " VALUES (%s);" % ', '.join(vfmt)
	log.debug(s)
	return (s, vl)
