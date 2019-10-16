# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_log(testing_log):
	with testing_log() as log:
		assert log.curLevel() == 'off'
