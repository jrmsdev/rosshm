# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

__all__ = ['connect', 'DatabaseError', 'IntegrityError']

connect = Mock()
DatabaseError = Mock()
IntegrityError = Mock()
