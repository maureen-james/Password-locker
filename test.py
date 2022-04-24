import unittest
from User import User # Importing the unittest module
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
    
    def test_save_User(self):
        """
        test_save_user test case to test if the user object is saved into
        the user_details
        """
        self.new_User.save_User()
        self.assertEqual(len(User.user_info),1)

    def tearDown(self):
        """
        cleans after test case has run
        """   
        User.user_info =[]

    def test_save_multiple_User(self):
        """
        to test if we can save multiple users
        """    
        self.new_User.save_User()
        test_User=User("Test","test","1234")
        test_User.save_User()
        self.assertEqual(len(User.user_info),2)


    def test_delete_User(self):

        """
            test_delete_user to test if we can remove a user from our user_list
        """
        self.new_User.save_User()
        test_User = User("Test","test","1234")
        test_User.save_User()
        self.new_User.delete_User()
        self.assertEqual(len(User.user_info),1)

    def test_display_Users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_Users(),User.user_info)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credentials = Credentials()   
    def  test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name,"Twitter")
        self.assertEqual(self.new_credentials.username,"Mwas")
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
        test_credentials= Credentials("instagram","@nyambura","98765")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_infomation),2)

    def test_delete_credentials(self):

        """
        test_delete_user to test if we can remove a user from our user_list
        """
        self.new_credentials.save_credentials()
        test_credentials= Credentials("instagram","@nyambura","98765")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()

    def test_display_credentials(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.user_infomation)

    def test_find_credential(self):

        '''
        test to check if we can return a Boolean  if we cannot find the credentialsusing account name.
        '''
        self.new_credentials.save_credentials()
        test_credential = Credentials("facebook", "mwas", "348767")   
        test_credential.save_credentials()

        the_credential = Credentials.find_credential("facebook")

        self.assertEqual(the_credential.account_name,test_credential.account_name)


    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credentials.save_credentials()
        the_credential = Credentials("facebook", "mwas", "348767")  
        the_credential.save_credentials()
        credential_is_found = Credentials.if_credential_exist("facebook")
        self.assertTrue(credential_is_found)



    def test_display_all_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.user_infomation)



if __name__ == '__main__':
    unittest.main()