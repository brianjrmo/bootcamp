import unittest
from user_management import User_Management

TEST_DOMAIN = "192.168.56.101"
CONFIG_FILE = "config.json"
class TestApp(unittest.TestCase):
    def setUp(self):
        """create a test object"""
        self.um = User_Management(CONFIG_FILE)
        self.um.set_db_host(TEST_DOMAIN)
        
        """test data definition"""
        self.name = 'Mani'
        
    def test_add_user(self):
        self.um.set_status(self.name,'DELETED')
        results = self.um.add(self.name)
        expected_results = ("User {} added".format(self.name), 200)
        self.assertEqual(results, expected_results)
    
    def test_find_user(self):
        self.um.add(self.name)
        results = self.um.find(self.name)
        expected_results = ("User found.", 200)
        self.assertEqual(results, expected_results)

    def test_login_user(self):
        self.um.add(self.name)
        results = self.um.set_status(self.name,'LOGON')
        expected_results = ('User {} LOGON'.format(self.name), 200)
        self.assertEqual(results, expected_results)

    def test_logout_user(self):
        self.um.add(self.name)
        results = self.um.set_status(self.name,'LOGOFF')
        expected_results = ('User {} LOGOFF'.format(self.name), 200)
        self.assertEqual(results, expected_results)
        
    def test_delete_user(self):
        self.um.add(self.name)
        results = self.um.set_status(self.name,'DELETED')
        expected_results = ('User {} DELETED'.format(self.name), 200)
        self.assertEqual(results, expected_results)
            
    def tearDown(self):
        self.um.set_status(self.name,'DELETED')
        del self.um
        
        
if __name__ == '__main__':
    unittest.main()