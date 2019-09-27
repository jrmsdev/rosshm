# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import subprocess as proc
from os import path, getenv, environ

from rosshm import log
from rosshm.cmd import flags
from rosshm.libdir import libdir
from rosshm.wapp import wapp

__all__ = ['main']

def main():
	args = flags.parse()
	cfgfn = path.abspath(args.config)

	if args.debug:
		return _debugMode(args, cfgfn)
	else:
		return _uwsgi(args, cfgfn)

def _debugMode(args, cfgfn):
	app = wapp.init(cfgfn = cfgfn)
	return app.run(host = '127.0.0.1', port = int(args.port),
		quiet = False, reloader = True, debug = True)

def _gethome():
	h = getenv('ROSSHM_HOME', None)
	if h is None:
		h = sys.exec_prefix
	return path.abspath(h)

def _uwsgi(args, cfgfn):
	rc = 0
	inifn = path.abspath(libdir / 'wapp' / 'uwsgi.ini')

	cmd = ('uwsgi', '--need-plugin', 'python3')
	cmd += ('--set-ph', f"rosshm-home={_gethome()}")

	if args.workers != '':
		cmd += ('--set-ph', f"rosshm-workers={args.workers}")
	if args.threads != '':
		cmd += ('--set-ph', f"rosshm-threads={args.threads}")

	if args.user != '':
		cmd += ('--set-ph', f"rosshm-user={args.user}")
	if args.group != '':
		cmd += ('--set-ph', f"rosshm-group={args.group}")

	cmd += ('--set-ph', f"rosshm-port={args.port}")

	cmd += ('--touch-reload', cfgfn)
	cmd += ('--ini', inifn)

	cmdenv = {'ROSSHM_CONFIG': cfgfn}

	try:
		log.debug(f"run {cmd}")
		log.debug(f"config {cfgfn}")
		proc.run(cmd, shell = False, env = cmdenv, check = True)
	except proc.CalledProcessError as err:
		log.error(f"{err}")
		rc = err.returncode
	except KeyboardInterrupt:
		rc = 128

	log.debug(f"exit {rc}")
	return rc

if __name__ == '__main__':
	sys.exit(main())
