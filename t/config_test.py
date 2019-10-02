# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import config

def test_config(testing_config):
	with testing_config():
		assert config.filename().endswith('rosshm.ini')

def test_database(testing_config):
	with testing_config():
		db = config.database()
		assert db['driver'] == 'sqlite'
		assert db['name'].endswith('rosshmdb.sqlite')
		assert db['config'] == ''
