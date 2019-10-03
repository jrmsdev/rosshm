# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from pathlib import Path

__all__ = ['tdata']

# test data paths manager
tdata = Path(path.abspath(path.join('.', 'tdata')))
