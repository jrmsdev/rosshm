# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import cmd

def test_flags(testing_cmd):
	with testing_cmd() as cmd:
		cmd.main([])
