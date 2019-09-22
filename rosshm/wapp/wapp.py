# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import Bottle

from rosshm import config

__all__ = ['init']

def init():
	config.init()
	return Bottle()
