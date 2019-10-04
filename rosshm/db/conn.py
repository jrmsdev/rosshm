# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm import log

class DBConn(object):

	def __init__(self, conn):
		log.debug('init')
		self._conn = conn
		self._cur = None
		self._closed = False

	def __del__(self):
		if not self._closed:
			self.close()

	def close(self):
		log.debug('close')
		if self._cur is not None:
			log.debug('close cursor')
			self._cur.close()
		log.debug('close connection')
		self._conn.close()
		self._closed = True

	def commit(self):
		log.debug('commit')
		self._conn.commit()

	def rollback(self):
		log.debug('rollback')
		self._conn.rollback()

	def execute(self, op, param = None):
		log.debug('execute')
		if self._cur is not None:
			log.debug('close cursor')
			self._cur.close()
			del self._cur
			self._cur = None
		self._cur = self._conn.cursor()
		if param is None:
			self._cur.execute(op)
		else:
			self._cur.execute(op, param)
		return self._cur
