# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from rosshm import config

def test_config(testing_config):
	with testing_config():
		assert config.filename().endswith('rosshm.ini')
		assert config.getbool('debug')

def test_database(testing_config):
	with testing_config():
		db = config.database()
		assert db['driver'] == 'sqlite'
		assert db['name'].endswith('rosshmdb.sqlite')
		assert db['config'] == ''
	with testing_config() as cfg:
		fn = path.join(path.sep, 'testing', 'db.cfg')
		cfg.set('rosshm', 'db.config', fn)
		db = config.database()
		assert db['config'] == fn
