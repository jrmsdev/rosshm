# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pathlib import Path

__all__ = ['libdir']

_srcdir = Path(__file__).parent

libdir = Path(_srcdir)
