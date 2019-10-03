# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import version

def test_version():
	s = 'testing version master (build devel)'
	assert version.get() == 'master'
	assert version.build() == 'devel'
	assert version.string('testing') == s
	assert version.string().startswith('%(prog)s version')
