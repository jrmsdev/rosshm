# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['fieldType']

# get fields type
def fieldType(fields, name):
	if name == 'pk':
		return int
	m = fields.get(name)
	return m[0]
