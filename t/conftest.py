# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock
import bottle

_bottle = Mock()

bottle.Bottle = _bottle.Bottle
bottle.Bottle.return_value = _bottle.wapp
bottle.redirect = _bottle.redirect
bottle.view = _bottle.view

import sys
from os import path

tlib = path.join(path.dirname(path.dirname(__file__)), 'tlib')
sys.path.insert(0, tlib)

from testing.conf import *
