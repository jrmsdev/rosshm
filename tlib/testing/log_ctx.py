# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from os import getenv
from unittest.mock import Mock

import rosshm.log

rosshm.log.init(getenv('ROSSHMTEST_LOG', 'off'))
rosshm.log.init = Mock()

_curlevel = rosshm.log._curlevel
_logger = rosshm.log._logger
_fmt = rosshm.log._fmt

@contextmanager
def log_ctx(level = 'off', colored = False):
	try:
		if colored:
			rosshm.log._fmt = rosshm.log._colorFmt()
		else:
			rosshm.log._fmt = rosshm.log._txtFmt()
		rosshm.log._logger = rosshm.log._sysLogger(level)
		rosshm.log._curlevel = level
		yield rosshm.log
	finally:
		del rosshm.log._curlevel
		rosshm.log._curlevel = _curlevel
		del rosshm.log._logger
		rosshm.log._logger = _logger
		del rosshm.log._fmt
		rosshm.log._fmt = _fmt
