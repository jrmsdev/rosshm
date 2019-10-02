# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_config(testing_config):
	cfg = testing_config()
	assert cfg is None
