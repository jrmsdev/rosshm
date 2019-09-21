# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import subprocess as sp
from os import path

from rosshm import log
from rosshm.cmd import flags

def main():
	args = flags.parse()
	cmd = (
	'uwsgi',
		'--need-plugin', 'python3',
		'--ini', path.expanduser(args.config),
	)
	try:
		log.debug(f"run {cmd}")
		sp.run(cmd, check = True)
	except sp.CalledProcessError as err:
		log.error(f"{err}")
		return err.returncode
	except KeyboardInterrupt:
		return 128
	return 0

if __name__ == '__main__':
	sys.exit(main())
