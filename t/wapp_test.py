# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_init(testing_wapp):
	with testing_wapp('wapp') as ctx:
		ctx.wapp.init()
		assert False