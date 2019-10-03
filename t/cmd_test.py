# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from subprocess import CalledProcessError

from rosshm import config
from rosshm.libdir import libdir

def test_debug(testing_cmd):
	with testing_cmd() as cmd:
		cmd.main(['--config', config.filename(), '--debug'])
		cmd.wapp.init.assert_called_with(cfgfn = config.filename())
		args = {'debug': True, 'host': '127.0.0.1', 'port': 3721,
			'quiet': False, 'reloader': True}
		cmd.wapp.mock_app.run.assert_called_with(**args)

def test_uwsgi(testing_cmd):
	inifn = str(libdir / 'wapp' / 'uwsgi.ini')
	with testing_cmd() as cmd:
		cmd.main([
			'--config', config.filename(),
			'--workers', '2',
			'--threads', '1',
			'--user', 'tuser',
			'--group', 'tgroup',
		])
		x = ('uwsgi', '--need-plugin', 'python3')
		x += ('--set-ph', "rosshm-home=%s" % path.join(path.sep, 'opt', 'rosshm'))
		x += ('--set-ph', 'rosshm-workers=2')
		x += ('--set-ph', 'rosshm-threads=1')
		x += ('--set-ph', 'rosshm-user=tuser')
		x += ('--set-ph', 'rosshm-group=tgroup')
		x += ('--set-ph', 'rosshm-port=3721')
		x += ('--touch-reload', config.filename())
		x += ('--ini', inifn)
		e = {'ROSSHM_CONFIG': config.filename()}
		cmd.proc.run.assert_called_with(x, check = True, env = e, shell = False)

def test_uwsgi_error(testing_cmd):
	with testing_cmd() as cmd:
		cmd.proc.run.side_effect = CalledProcessError(9, 'testing')
		rc = cmd.main(['--config', config.filename()])
		assert rc == 9
	with testing_cmd() as cmd:
		cmd.proc.run.side_effect = KeyboardInterrupt()
		rc = cmd.main(['--config', config.filename()])
		assert rc == 128
