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

    def test_save_multiple_user(self):
        """
        to test if we can save multiple users
        """    
        self.new_user.save_user()
        test_user=User("Test","1234")
        test_user.save_user()
        self.assertEqual(len(User.user_info),2)


    def test_delete_user(self):

        """
            test_delete_user to test if we can remove a user from our user_list
        """
        self.new_user.save_user()
        test_user = User("Test","1234")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_info),1)

    def test_display_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(),User.user_info)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credentials = Credentials("Facebook","12345")   
    def  test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name,"Facebook")
        self.assertEqual(self.new_credentials.password,"12345")
    def test_save_credentials(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user_details
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_infomation),1)        
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credentials.user_infomation = []
    def test_save_multiple_credentials(self):
        """
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        """
        self.new_credentials.save_credentials()
        test_credentials= Credentials("instagram","@ajedidah_","31526673")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_infomation),2)
        

        



if __name__ == '__main__':
    unittest.main()