# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import subprocess as proc
from os import path, getenv

from rosshm import log
from rosshm.cmd import flags

__all__ = ['main']

def _gethome():
	h = getenv('ROSSHM_HOME', None)
	if h is None:
		h = sys.exec_prefix
	return path.abspath(h)

def main():
	args = flags.parse()
	cfgfn = path.abspath(path.expanduser(args.config))
	cmd = (
	'uwsgi',
		'--need-plugin', 'python3',
		'--set-ph', f"rosshm-home={_gethome()}",
		'--touch-reload', cfgfn,
		'--ini', cfgfn,
	)
	cmdenv = {'ROSSHM_CONFIG': cfgfn}
	try:
		log.debug(f"run {cmd}")
		proc.run(cmd, shell = False, env = cmdenv, check = True)
	except proc.CalledProcessError as err:
		log.error(f"{err}")
		return err.returncode
	except KeyboardInterrupt:
		return 128
	return 0

if __name__ == '__main__':
	sys.exit(main())
