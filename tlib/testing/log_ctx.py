# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock

@contextmanager
def log_ctx():
	try:
		yield
	finally:
		pass
