# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import re

from rosshm import version

def test_version():
	if version.get() == 'master':
		s = 'testing version master (build devel)'
		assert version.build() == 'devel'
		assert version.string('testing') == s
		assert version.string().startswith('%(prog)s version')
	else:
		assert re.match(r'\d+\.\d+', version.get())
		assert re.fullmatch(r'\d\d\d\d\d\d\.\d\d\d\d\d\d', version.build())
		assert re.match(r'testing version \d+\.\d+', version.string('testing'))
