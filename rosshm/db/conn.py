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
			self.close(nolog = True)

	def close(self, nolog = False):
		if not nolog: log.debug('close')
		if self._cur is not None:
			if not nolog: log.debug('close cursor')
			self._cur.close()
			self._cur = None
		if not nolog: log.debug('close connection')
		self._conn.close()
		self._closed = True

	def commit(self):
		log.debug('commit')
		self._conn.commit()

	def rollback(self):
		log.debug('rollback')
		self._conn.rollback()

	def execute(self, op, param = tuple()):
		if self._cur is None:
			log.debug('new cursor')
			self._cur = self._conn.cursor()
		log.debug('execute')
		self._cur.execute(op, param)
		return self._cur
