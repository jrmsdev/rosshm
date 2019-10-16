# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_log(testing_log):
	with testing_log() as log:
		assert log.curLevel() == 'off'

def test_fmt(testing_log):
	with testing_log() as log:
		assert log.curLevel() == 'off'
		assert isinstance(log._fmt, log._txtFmt)
	# ~ with testing_log(colored = True) as log:
		# ~ assert isinstance(log._fmt, log._colorFmt)
	# ~ with testing_log(colored = False) as log:
		# ~ assert isinstance(log._fmt, log._txtFmt)

def test_levels(testing_log):
	with testing_log() as log:
		assert log.curLevel() == 'off'
		assert isinstance(log._fmt, log._txtFmt)
		assert log.defaultLevel() == 'warn'
		assert sorted(log.levels()) == ['debug', 'error', 'info', 'off', 'quiet', 'warn']

def test_debug(testing_log):
	with testing_log('debug') as log:
		assert log.curLevel() == 'debug'
		assert isinstance(log._fmt, log._txtFmt)

def test_error(testing_log):
	with testing_log('error') as log:
		assert log.curLevel() == 'error'
		assert isinstance(log._fmt, log._txtFmt)

def test_info(testing_log):
	with testing_log('info') as log:
		assert log.curLevel() == 'info'
		assert isinstance(log._fmt, log._txtFmt)

def test_quiet(testing_log):
	with testing_log('quiet') as log:
		assert log.curLevel() == 'quiet'
		assert isinstance(log._fmt, log._txtFmt)

def test_warn(testing_log):
	with testing_log('warn') as log:
		assert log.curLevel() == 'warn'
		assert isinstance(log._fmt, log._txtFmt)
