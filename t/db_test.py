# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import config

def test_config(testing_db):
	with testing_db():
		cfg = config.database()
		assert cfg['driver'] == 'sqlite'
		assert cfg['config'] == ''
		assert cfg['name'] == ':memory:'
