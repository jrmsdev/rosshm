# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from rosshm import log
from rosshm.libdir import libdir

__all__ = ['serve']

_rootdir = path.abspath(libdir / 'static')
_serveExtension = {
	'.css': True,
}

def serve(filename):
	"""serve static files"""
	filename = path.normpath(filename)
	ext = path.splitext(filename)[1]
	if ext == '' or filename.startswith('.') or \
		not _serveExtension.get(ext, False):
		log.warn(f"static file refuse '{filename}'")
		return bottle.HTTPError(404, "file not found")
	log.debug(f"serve {filename}")
	return bottle.static_file(filename, root = _rootdir)
