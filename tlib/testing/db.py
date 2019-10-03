# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest
from contextlib import contextmanager
from unittest.mock import Mock

from testing.config import config_ctx

__all__ = ['testing_db', 'db_ctx']

@contextmanager
def db_ctx():
	try:
		with config_ctx() as cfg:
			cfg.set('rosshm', 'db.name', ':memory:')
			yield
	finally:
		pass

@pytest.fixture
def testing_db():
	return db_ctx
