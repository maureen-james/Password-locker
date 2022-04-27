import random
import string

class User:
     """
     stores users info.

     """
     user_info = []
     def __init__(self,username,password):
       self.username=username
       self.password=password
      
     def save_User(self):
      """
      saves user infomation.
      """  
      User.user_info.append(self)

     def delete_User(self):
      """
      deletes users' saved infomation.
      """  
      User.user_info.remove(self)
     
     @classmethod
     def display_Users(cls):
        '''
        returns the user list
        '''
        return cls.user_info

     @classmethod
     def find_Users(cls,username):
        '''
        returns the user list
        '''
        for User in cls.user_info:
            if User.username == username:
                return User
        


class Credentials:
     """
     stores users credentials.
     
     """
     user_infomation = []
     def __init__(self,account_name,username,password):
        """
        defines user credentials
        """
        self.account_name = account_name
        self.username = username
        self.password = password    

     def save_credentials(self):
      """
      saves users credentials
      """ 
      Credentials.user_infomation.append(self)

     def delete_credentials(self):
      """
      deletes users credentials when needed to 
      """  
      Credentials.user_infomation.remove(self)

     @classmethod
     def display_credentials(cls):
      """
      return user information
      """ 
      return cls.user_infomation

     @classmethod
     def find_credentials(cls,account_name):
        """
     takes in account_name and returns a credentials that matches with that account_name.
        """
        for Credentials in cls.user_infomation:
            if Credentials.account_name == account_name:
                return Credentials

    
     @classmethod
     def if_credentials_exist(cls, account_name):
        """
        checks if a credential exists 
        """
        for Credentials in cls.user_infomation:
            if Credentials.account_name == account_name:
                return True
        return False

     @classmethod
     def display_credentials(cls):
        """
        return all items in the user information
        """
        return cls.user_infomation

    
     def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))

    
          