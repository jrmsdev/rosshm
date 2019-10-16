# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises

def test_log(testing_log):
	with testing_log() as log:
		assert log.curLevel() == 'off'

def test_fmt(testing_log):
	with testing_log() as log:
		assert log.curLevel() == 'off'
		assert isinstance(log._fmt, log._txtFmt)
	with testing_log(colored = True) as log:
		assert isinstance(log._fmt, log._colorFmt)
	with testing_log(colored = False) as log:
		assert isinstance(log._fmt, log._txtFmt)

def test_colored(testing_log):
	with testing_log() as log:
		log.init_orig('off', colored = True)
		assert isinstance(log._fmt, log._colorFmt)

def test_levels(testing_log):
	with testing_log() as log:
		assert log.curLevel() == 'off'
		assert isinstance(log._fmt, log._txtFmt)
		assert log.defaultLevel() == 'warn'
		assert sorted(log.levels()) == ['debug', 'error', 'info', 'off', 'quiet', 'warn']
		assert not log.debugEnabled()

def test_invalid_level(testing_log):
	with testing_log() as log:
		with raises(RuntimeError, match = 'invalid log level: testing'):
			log._sysLogger('testing')

def test_debug(testing_log):
	with testing_log('debug') as log:
		assert log.curLevel() == 'debug'
		assert isinstance(log._fmt, log._txtFmt)
		assert log.debugEnabled()
		log.debug('testing')
	msg = log.outs.read()
	assert msg.startswith('D: ')
	assert msg.endswith(': testing\n')

def test_error(testing_log):
	with testing_log('error') as log:
		assert log.curLevel() == 'error'
		assert isinstance(log._fmt, log._txtFmt)
		log.error('testing')
	msg = log.outs.read()
	assert msg.startswith('E: ')
	assert msg.endswith(': testing\n')

def test_info(testing_log):
	with testing_log('info') as log:
		assert log.curLevel() == 'info'
		assert isinstance(log._fmt, log._txtFmt)
		log.info('testing')
	msg = log.outs.read()
	assert msg.startswith('I: ')
	assert msg.endswith(': testing\n')

def test_quiet(testing_log):
	with testing_log('quiet') as log:
		assert log.curLevel() == 'quiet'
		assert isinstance(log._fmt, log._txtFmt)
		log.msg('testing')
	msg = log.outs.read()
	assert msg == ''

def test_warn(testing_log):
	with testing_log('warn') as log:
		assert log.curLevel() == 'warn'
		assert isinstance(log._fmt, log._txtFmt)
		log.warn('testing')
	msg = log.outs.read()
	assert msg.startswith('W: ')
	assert msg.endswith(': testing\n')

def test_msg(testing_log):
	with testing_log('warn') as log:
		assert log.curLevel() == 'warn'
		assert isinstance(log._fmt, log._txtFmt)
		log.msg('testing')
	msg = log.outs.read()
	assert msg == 'testing\n'

def test_dummy(testing_log):
	with testing_log() as log:
		l = log._dummyLogger()
		l.debug('testing')
		l.error('testing')
		l.warn('testing')
		l.info('testing')
		l.msg('testing')
