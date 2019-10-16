# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from os import path, getpid

# colors

class _txtFmt(object):
	debug = lambda self, msg: 'D: ' + msg
	warn = lambda self, msg: 'W: ' + msg
	error = lambda self, msg: 'E: ' + msg
	info = lambda self, msg: 'I: ' + msg
	msg = lambda self, msg: msg

_cyan = '\033[0;36m'
_red = '\033[0;31m'
_yellow = '\033[0;33m'
_blue = '\033[0;34m'
_green = '\033[0;32m'
_grey = '\033[1;30m'
_reset = '\033[0m'

class _colorFmt(object):
	debug = lambda self, msg: _grey + msg + _reset
	error = lambda self, msg: _red + msg + _reset
	warn = lambda self, msg: _yellow + msg + _reset
	info = lambda self, msg: _blue + msg + _reset
	msg = lambda self, msg: _green + msg + _reset

# debug file info

_idx = __file__.find('log.py')

def _getCaller(depth):
	inf = sys._getframe(depth)
	return "%s:%d" % (inf.f_code.co_filename[_idx:], inf.f_lineno)

# setup logger

class _sysLogger(object):

	def __init__(self, level, outs = None, flush = True):
		self._depth = 3
		self._pid = getpid()
		self._outs = sys.stdout
		self._errs = sys.stderr
		self._flush = flush
		if outs is not None:
			self._outs = outs
			self._errs = outs
		self.debug = self._off
		self.warn = self._off
		self.error = self._off
		self.info = self._off
		self.msg = self._off
		self._initLevel(level)

	def _initLevel(self, level):
		# all messages
		if level == 'debug':
			self.debug = self._debug
			self.info = self._info
			self.msg = self._msg
			self.warn = self._warn
			self.error = self._error
		# info + msg + warn + error
		elif level == 'info':
			self.debug = self._off
			self.info = self._info
			self.msg = self._msg
			self.warn = self._warn
			self.error = self._error
		#  msg + warn + error
		elif level == 'warn':
			self.debug = self._off
			self.info = self._off
			self.msg = self._msg
			self.warn = self._warn
			self.error = self._error
		# msg + error
		elif level == 'error':
			self.debug = self._off
			self.info = self._off
			self.msg = self._msg
			self.warn = self._off
			self.error = self._error
		# errors only
		elif level == 'quiet':
			self.debug = self._off
			self.info = self._off
			self.msg = self._off
			self.warn = self._off
			self.error = self._error
		# no messages
		elif level == 'off':
			self.debug = self._off
			self.info = self._off
			self.msg = self._off
			self.warn = self._off
			self.error = self._off
		else:
			raise RuntimeError("invalid log level: %s" % level)

	def _off(self, msg):
		pass

	def _debug(self, msg):
		caller = _getCaller(self._depth)
		print(_fmt.debug("[%d] %s: %s" % (self._pid, caller, msg)),
			file = self._errs, flush = self._flush)

	def _error(self, msg):
		print(_fmt.error(msg), file = self._errs, flush = self._flush)

	def _warn(self, msg):
		print(_fmt.warn(msg), file = self._errs, flush = self._flush)

	def _info(self, msg):
		print(_fmt.info(msg), file = self._outs, flush = self._flush)

	def _msg(self, msg):
		print(_fmt.msg(msg), file = self._outs, flush = self._flush)

class _dummyLogger(object):

	def debug(self, msg):
		pass

	def error(self, msg):
		pass

	def warn(self, msg):
		pass

	def info(self, msg):
		pass

	def msg(self, msg):
		pass

_fmt = _txtFmt()
_logger = _dummyLogger()
_curlevel = None

# public methods

__all__ = ['init', 'levels', 'defaultLevel', 'curLevel', 'debugEnabled',
	'debug', 'error', 'warn', 'info', 'msg']

def init(level, colored = None, outs = None):
	global _fmt
	global _logger
	global _curlevel
	if colored is None:
		colored = sys.stdout.isatty() and sys.stderr.isatty()
	if colored:
		_fmt = None
		_fmt = _colorFmt()
	_logger = None
	_logger = _sysLogger(level, outs = outs)
	_curlevel = None
	_curlevel = level

def levels():
	return ['debug', 'info', 'warn', 'error', 'quiet', 'off']

def defaultLevel():
	return 'warn'

def curLevel():
	return _curlevel

def debugEnabled():
	return _curlevel == 'debug'

def debug(msg):
	_logger.debug(msg)

def error(msg):
	_logger.error(msg)

def warn(msg):
	_logger.warn(msg)

def info(msg):
	_logger.info(msg)

def msg(msg):
	_logger.msg(msg)
