# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest
from os import path

from rosshm import config

__all__ = ['testing_config']

@pytest.fixture
def testing_config():
	def wrapper():
		return None
	return wrapper
