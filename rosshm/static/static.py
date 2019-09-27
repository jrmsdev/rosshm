# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from rosshm.libdir import libdir

__all__ = ['serve']

_rootdir = path.abspath(libdir / 'static')
_serveExtension = {
	'.css': True,
}

def serve(filename):
	filename = path.normpath(filename)
	ext = path.splitext(filename)[1]
	if filename.startswith('.'):
		return bottle.HTTPError(404, "file not found")
	if ext == '' or not _serveExtension.get(ext, False):
		return bottle.HTTPError(404, "file not found")
	return bottle.static_file(filename, root = _rootdir)
