# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock

from rosshm import log

@contextmanager
def log_ctx(level = 'off'):
	_curlevel = log._curlevel
	_logger = log._logger
	_fmt = log._fmt
	try:
		log.init_orig(level)
		yield log
	finally:
		del log._curlevel
		log._curlevel = _curlevel
		del log._logger
		log._logger = _logger
		del log._fmt
		log._fmt = _fmt
