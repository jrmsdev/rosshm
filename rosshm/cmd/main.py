# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import subprocess as proc
from os import path, getenv

from rosshm import log
from rosshm.cmd import flags
from rosshm.libdir import libdir

__all__ = ['main']

def _gethome():
	h = getenv('ROSSHM_HOME', None)
	if h is None:
		h = sys.exec_prefix
	return path.abspath(h)

def main():
	args = flags.parse()
	cfgfn = path.abspath(args.config)
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
		return err.returncode
	except KeyboardInterrupt:
		return 128

	return 0

if __name__ == '__main__':
	sys.exit(main())
