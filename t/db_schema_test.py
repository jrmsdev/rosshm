# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from testing.db.schema import DBTesting

db_t = DBTesting()

def test_set_get(testing_db):
	with testing_db(db_t = True) as conn:
		assert not db_t.get(conn, pk = 0)
		db_t.set(conn, option = 't1', value = 'v1')
		row = db_t.get(conn, 'option', 'value', pk = 1)
		assert row['option'] == 't1'
		assert row['value'] == 'v1'
