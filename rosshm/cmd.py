# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

from . import flags

def main():
	args = flags.parse()
	return 0

if __name__ == '__main__':
	sys.exit(main())
