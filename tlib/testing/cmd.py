# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest
from contextlib import contextmanager
from unittest.mock import Mock

from rosshm.cmd import main as cmd_main
from testing.config import config_ctx

__all__ = ['testing_cmd', 'cmd_ctx']

@contextmanager
def cmd_ctx():
	proc = cmd_main.proc
	wapp = cmd_main.wapp
	with config_ctx():
		try:
			cmd_main.proc.run = Mock()
			cmd_main.wapp = Mock()
			cmd_main.wapp.init = Mock()
			cmd_main.wapp.mock_app = Mock()
			cmd_main.wapp.init.return_value = cmd_main.wapp.mock_app
			yield cmd_main
		finally:
			del cmd_main.proc
			cmd_main.proc = proc
			del cmd_main.wapp
			cmd_main.wapp = wapp

@pytest.fixture
def testing_cmd():
	return cmd_ctx
