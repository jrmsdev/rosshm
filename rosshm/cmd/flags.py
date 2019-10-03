# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import argparse

from rosshm import log, version

__all__ = ['parse']

_desc = 'ross, the house master'

def _new():
	p = argparse.ArgumentParser(prog = 'rosshm', description = _desc)
	p.add_argument('-V', '--version', help = 'show version and exit',
		action = 'version', version = version.string())
	p.add_argument('--debug', help = 'enable debug settings',
		action = 'store_true', default = False)
	p.add_argument('--log', help = ', '.join(log.levels()), metavar = 'level',
		default = log.defaultLevel(), choices = log.levels())
	p.add_argument('--config', help = '~/.config/rosshm.ini',
		metavar = 'filename', default = '~/.config/rosshm.ini')
	p.add_argument('--workers', help = 'number of CPU(s)',
		metavar = 'number', default = '')
	p.add_argument('--threads', help = 'number of CPU(s)',
		metavar = 'number', default = '')
	p.add_argument('--user', help = 'current user',
		metavar = 'name', default = '')
	p.add_argument('--group', help = 'current user group',
		metavar = 'name', default = '')
	p.add_argument('--port', help = '3721',
		metavar = 'number', default = '3721')
	return p

def parse(argv):
	p = _new()
	args = p.parse_args(args = argv)
	if args.debug:
		log.init('debug')
	else:
		log.init(args.log)
	log.debug(f"rosshm version {version.get()}")
	log.debug(f"config {args.config}")
	return args
