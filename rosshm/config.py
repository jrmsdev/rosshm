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
		'db.driver': 'sqlite',
		'db.name': 'rosshmdb',
		'db.config': '',
		'static.enable': True,
		'web.enable': True,
	},
)

_cfgfn = getenv('ROSSHM_CONFIG',
	path.expanduser(path.join('~', '.config', 'rosshm.ini')))

def init(fn = _cfgfn):
	global _cfgfn
	fn = path.abspath(fn)
	if path.isfile(fn):
		with open(fn, 'r') as fh:
			_cfg.read_file(fh)
	_cfgfn = fn
	if not _cfg.has_section('rosshm'):
		_cfg.add_section('rosshm')

def filename():
	global _cfgfn
	return _cfgfn

def database():
	drv = get('db.driver')
	name = get('db.name')
	if drv == 'sqlite':
		name = path.abspath(path.join(get('datadir'), f"{name}.{drv}"))
	cfg = get('db.config')
	if cfg != '':
		cfg = path.abspath(path.expanduser(cfg))
	return {
		'driver': drv,
		'name': name,
		'config': cfg,
	}

def get(option, **kwargs):
	return _cfg.get('rosshm', option, **kwargs)

def getbool(option, **kwargs):
	return _cfg.getboolean('rosshm', option, **kwargs)
