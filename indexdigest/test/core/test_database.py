from __future__ import print_function

from unittest import TestCase

from indexdigest.database import DatabaseBase, Database


class DatabaseTestMixin(object):
    DSN = 'mysql://index_digest:qwerty@localhost/index_digest'

    @property
    def connection(self):
        return Database.connect_dsn(self.DSN)


class TestDatabaseBase(TestCase, DatabaseTestMixin):

    def test_database_connect(self):
        conn = DatabaseBase(host='localhost', user='index_digest', passwd='qwerty', db='index_digest')
        self.assertIsInstance(conn, DatabaseBase)

    def test_database_connect_dsn(self):
        self.assertIsInstance(self.connection, DatabaseBase)

    def test_query_list(self):
        res = list(self.connection.query_list('SHOW DATABASES'))

        self.assertTrue('information_schema' in res, res)
        self.assertTrue('index_digest' in res, res)


class TestDatabase(TestCase, DatabaseTestMixin):

    def test_database_version(self):
        version = self.connection.get_server_info()  # 5.5.57-0+deb8u1

        self.assertTrue(version.startswith('5.'), 'MySQL server should be from 5.x line')

    def test_tables(self):
        tables = list(self.connection.tables())
        print(tables)

        self.assertTrue('0000_the_table' in tables)

    def test_variables(self):
        variables = self.connection.variables()
        print(variables)

        self.assertTrue('version_compile_os' in variables)
        self.assertTrue('innodb_version' in variables)

    def test_variables_like(self):
        variables = self.connection.variables(like='innodb')
        print(variables)

        self.assertFalse('version_compile_os' in variables)  # this variable does not match given like
        self.assertTrue('innodb_version' in variables)
