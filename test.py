import unittest
from User import User,Credentials # Importing the unittest module




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
        self.new_User = User("Maureen","0712345678") # create user object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_User.username,"Maureen")
        self.assertEqual(self.new_User.password,"0712345678")
    
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
        test_User=User("Test","1234")
        test_User.save_User()
        self.assertEqual(len(User.user_info),2)


    def test_delete_User(self):

        """
            test_delete_user to test if we can remove a user from our user_list
        """
        self.new_User.save_User()
        test_User = User("Test","1234")
        test_User.save_User()
        self.new_User.delete_User()
        self.assertEqual(len(User.user_info),1)

    def test_display_Users(self):
        """
        returns a list of all users saved
        """
        self.assertEqual(User.display_Users(),User.user_info)

class TestCredentials(unittest.TestCase):

     def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credentials = Credentials("Facebook","Mwas","12345")   
     def  test_init(self):
         '''
          test_init test case to test if the object is initialized properly
         '''
         self.assertEqual(self.new_credentials.account_name,"Facebook")
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
         objects to our user information
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
         returns a list of all users saved
         """
         self.assertEqual(Credentials.display_credentials(),Credentials.user_infomation)

     def test_find_credentials(self):

         '''
         test to check if we can return a Boolean  if we cannot find the credentials using account name.
         '''
         self.new_credentials.save_credentials()
         test_credentials = Credentials("facebook", "mwas", "348767")   
         test_credentials.save_credentials()

         the_credentials = Credentials.find_credentials("facebook")

         self.assertEqual(the_credentials.account_name,test_credentials.account_name)


     def test_credentials_exist(self):
         """
         test to check if we can return a true or false based on whether we find or can't find the credential.
         """
         self.new_credentials.save_credentials()
         the_credentials = Credentials("facebook", "mwas", "348767")  
         the_credentials.save_credentials()
         credentials_is_found = Credentials.if_credentials_exist("facebook")
         self.assertTrue(credentials_is_found)



     def test_display_all_credentials(self):
         '''
         displays all the credentials that has been saved by the user
         '''

         self.assertEqual(Credentials.display_credentials(),Credentials.user_infomation)



if __name__ == '__main__':
    unittest.main()