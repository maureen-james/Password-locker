import unittest

from User import User # Importing the unittest module
User # Importing the contact class
from Credentials import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("Maureen","Mwangi","0712345678",) # create user object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_User.f_name,"Maureen")
        self.assertEqual(self.new_User.l_name,"Mwangi")
        self.assertEqual(self.new_User.p_number,"0712345678")
    
    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
        the user_details
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_info),1)

    def tearDown(self):
        """
        cleans after test case has run
        """   
        User.user_info =[]

        



if __name__ == '__main__':
    unittest.main()