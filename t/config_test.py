# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

def test_config(testing_config):
	with testing_config() as config:
		assert config.filename().endswith('rosshm.ini')
		assert config.getbool('debug')
	with testing_config(init = False):
		config.init(fn = None)
		assert config.getbool('debug')

def test_database(testing_config):
	with testing_config() as config:
		db = config.database()
		assert db['driver'] == 'sqlite'
		assert db['name'].endswith('rosshmdb.sqlite')
		assert db['config'] == ''
	with testing_config() as config:
		fn = path.join(path.sep, 'testing', 'db.cfg')
		config._cfg.set('rosshm', 'db.config', fn)
		db = config.database()
		assert db['config'] == fn
