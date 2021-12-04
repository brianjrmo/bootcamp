# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:26:23 2021

@author: brian
"""
import unittest
from user_management import UserManagement

TEST_DOMAIN = "192.168.56.101"
CONFIG_FILE = "config.json"
class TestApp(unittest.TestCase):
    """setup environment"""
    def setUp(self):
        """create a test object"""
        self.user_management = UserManagement(CONFIG_FILE)
        self.user_management.set_db_host(TEST_DOMAIN)

        #test data definition
        self.name = 'Mani'


    def test_add_user(self):
        """test add user function"""
        self.user_management.set_status(self.name, 'DELETED')
        results = self.user_management.add(self.name)
        expected_results = ("User {} added".format(self.name), 200)
        self.assertEqual(results, expected_results)

    def test_find_user(self):
        """test find user function"""
        self.user_management.add(self.name)
        results = self.user_management.find(self.name)
        expected_results = ("User found.", 200)
        self.assertEqual(results, expected_results)

    def test_login_user(self):
        """test login function"""
        self.user_management.add(self.name)
        results = self.user_management.set_status(self.name, 'LOGON')
        expected_results = ('User {} LOGON'.format(self.name), 200)
        self.assertEqual(results, expected_results)

    def test_logout_user(self):
        """test logout function"""
        self.user_management.add(self.name)
        results = self.user_management.set_status(self.name, 'LOGOFF')
        expected_results = ('User {} LOGOFF'.format(self.name), 200)
        self.assertEqual(results, expected_results)

    def test_delete_user(self):
        """test delete user function"""
        self.user_management.add(self.name)
        results = self.user_management.set_status(self.name, 'DELETED')
        expected_results = ('User {} DELETED'.format(self.name), 200)
        self.assertEqual(results, expected_results)

    def tearDown(self):
        self.user_management.set_status(self.name, 'DELETED')
        del self.user_management


if __name__ == '__main__':
    unittest.main()
    