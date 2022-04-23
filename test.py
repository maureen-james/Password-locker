import unittest

from User import User # Importing the unittest module
User # Importing the contact class

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

        self.assertEqual(self.new_contact.f_name,"Maureen")
        self.assertEqual(self.new_contact.l_name,"Mwangi")
        self.assertEqual(self.new_contact.p_number,"0712345678")



if __name__ == '__main__':
    unittest.main()