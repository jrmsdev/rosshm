# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser, ExtendedInterpolation
from os import getenv, path

__all__ = ['init', 'filename', 'get', 'getbool']

_cfg = ConfigParser(
	delimiters = ('=',),
	comment_prefixes = ('#', ';'),
	default_section = 'default',
	allow_no_value = False,
	strict = False,
	interpolation = ExtendedInterpolation(),
	defaults = {
		'debug': False,
		'datadir': path.expanduser(path.join('~', '.local', 'rosshm')),
		'log.level': 'warn',
		'core.enable': True,
		'web.enable': True,
	},
)

_cfgfn = None

def init(fn = None):
	global _cfgfn
	if fn is None:
		fn = getenv('ROSSHM_CONFIG',
			path.expanduser(path.join('~', '.config', 'rosshm.ini')))
	fn = path.abspath(fn)
	with open(fn, 'r') as fh:
		_cfg.read_file(fh)
	_cfgfn = fn
	if not _cfg.has_section('rosshm'):
		_cfg.add_section('rosshm')

def filename():
	global _cfgfn
	if _cfgfn is None:
		raise RuntimeError('config filename not set')
	return _cfgfn

def get(option, **kwargs):
	return _cfg.get('rosshm', option, **kwargs)

def getbool(option, **kwargs):
	return _cfg.getboolean('rosshm', option, **kwargs)
