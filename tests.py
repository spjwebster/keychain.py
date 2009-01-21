"""Test suite for the keychain class"""

import unittest
import keychain
from keychain import KeychainException

class KeychainTestCase(unittest.TestCase):

    """Set of tests for the keychain class"""
    
    def assert_equal(self, result, expected):
        """Wraps assertEqual for convenience"""
        return self.assertEqual(
            result, 
            expected,
            "%s should be %s" % (result, expected,),
        )

    def setUp(self):
        """Instantiates the keychain class and creates test keychain"""

        self.keychain = keychain.Keychain()
        self.test_keychain_name = 'keychain-py-test-suite'

    def tearDown(self):
        """Deletes the test keychain"""
        try:
            self.keychain.delete_keychain(self.test_keychain_name)
        except KeychainException:
            pass
        self.keychain = None

    def test_keychain_name_validation(self):
        """test keychain name"""
        keychain_name = self.keychain.normalise_keychain_name("test")
        self.assert_equal(keychain_name, "test")
        
    def test_keychain_name_validation2(self):
        """test keychain name when already ending with .keychain"""
        keychain_name = self.keychain.normalise_keychain_name("test.keychain")
        self.assert_equal(keychain_name, "test")

    def test_keychain_deletion(self):
        """Testing that keychain gets successfully deleted"""
        
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        deletion = self.keychain.delete_keychain(self.test_keychain_name)
        self.assert_equal(deletion, (True, 'Keychain deleted successfully'))
        

    def test_keychain_creation(self):

        """ Test keychain creation is successful

        Create a keychain and then attempt to find it in the list of
        keychains

        """
        creation = self.keychain.create_keychain(
            self.test_keychain_name, 'testpass'
        )
        self.assert_equal(creation, (True, 'Keychain created successfully'))
        
        
    def test_keychain_checking(self):
        """ Tests that checking for the test keychain finds it."""
        
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')   
        test_keychain = self.keychain.check_keychain_exists(
            self.test_keychain_name
        )
        self.assert_equal(test_keychain, True)
        
    def test_keychain_name_list(self):
        
        """Testing the list function contains the test keychain"""  
        
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        kc_list = self.keychain.list_keychains()
        self.assert_(
            self.test_keychain_name in kc_list, 
            "%s not in %s" % (self.test_keychain_name, kc_list)
        )
        
    def test_set_generic_password(self):
        
        """Test the creation of generic passwords"""
        
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        password = self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account', 
            'test-password', 
        )   
        self.assert_equal(
            password,
            (True, 'Password added to %s successfully' % \
                self.test_keychain_name)
        )
        
    def test_get_generic_password(self):

        """Test the retrieval of generic passwords with servicename"""

        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account',
            'test-password',
        )   
        account = self.keychain.get_generic_password(
            self.test_keychain_name, 'test-account'
        )
        self.assert_equal(
            account,
            { "account": 'test-account',"password": 'test-password' }
        )    

    def test_set_generic_password_with_servicename(self):        
        """Test the creation of generic passwords"""
        
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        password = self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account', 
            'test-password',
            'test-service'
        )   
        self.assert_equal(
            password,
            (True, 'Password added to %s successfully' % \
                self.test_keychain_name)
        )
        
    def test_get_generic_password_with_servicename(self):

        """Test the retrieval of generic passwords with servicename"""

        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account',
            'test-password',
            'test-service'
        )   
        account = self.keychain.get_generic_password(
            self.test_keychain_name, 'test-account', 'test-service'
        )
        self.assert_equal(
            account,
            { "account": 'test-account',"password": 'test-password',"service": 'test-service' }
        )    

        
    def test_show_keychain_info(self):
        """test displaying the default keychain info"""
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        result = self.keychain.show_keychain_info(self.test_keychain_name,)
        self.assert_equal(int(result['timeout']), 300)
        self.assert_equal(result['lock-on-sleep'], True)

        
        
    def test_changing_keychain_info(self):
        """test changing the default keychain info"""
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        self.keychain.set_keychain_settings(
            self.test_keychain_name, False, timeout=100
        )
        result = self.keychain.show_keychain_info(self.test_keychain_name,)
        self.assert_equal(int(result['timeout']), 100)
        self.assert_equal(result.get('lock-on-sleep', None), None)
        
    def test_list_generic_passwords(self):
        """test listing generic passwords"""
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account',
            'test-password',
            servicename="awesome1",
        )
        self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account2',
            'test-password2',
        )
        pass_list = self.keychain.list_keychain_accounts(
            self.test_keychain_name
        )
        self.assert_equal(pass_list, [
            {
                'account': 'test-account', 
                'password': 'test-password', 
                'service': 'awesome1'
            }, 
            {
                'account': 'test-account2', 
                'password': 'test-password2', 
            }
        ])

    def test_removing_generic_password(self):
        """test removing generic password"""

        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account',
            'test-password',
            servicename="awesome1",
        )
        self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account2',
            'test-password2',
        )
        self.keychain.remove_generic_password(
            self.test_keychain_name, 
            "testpass", "test-account2"
        )
        result = self.keychain.list_keychain_accounts(self.test_keychain_name)
        self.assert_equal(result, [
            {
                'account': 'test-account', 
                'password': 'test-password', 
                'service': 'awesome1'
            }
        ])

    def test_change_generic_password(self):
        """Test updating generic password"""
        
        self.keychain.create_keychain(self.test_keychain_name, 'testpass')
        self.keychain.set_generic_password(
            self.test_keychain_name, 
            'test-account',
            'test-password',
            servicename="awesome1",
        )
        self.keychain.change_generic_password(
            self.test_keychain_name, 
            'testpass',
            'test-account',
            'test-password-new',
        )
        result = self.keychain.list_keychain_accounts(self.test_keychain_name)
        self.assert_equal(result, [
            {
                'account': 'test-account', 
                'password': 'test-password-new', 
                'service': 'awesome1'
            }
        ])

suite = unittest.TestLoader().loadTestsFromTestCase(KeychainTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
