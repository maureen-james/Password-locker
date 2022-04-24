import random
import string

class Credentials:
     """
     stores users credentials.
     
     """
     user_infomation = []

def __init__(self,account_name,username,password):
    self.account_name=account_name
    self.username=username
    self.password=password

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
    return cls.user_information

@classmethod
def find_credentials(cls, account_name):
        """
     takes in account_name and returns a credentials that matches with that account_name.
        """
        for credentials in cls.user_information:
            if credentials.account_name == account_name:
                return credentials

    
@classmethod
def if_credentials_exist(cls, account_name):
        """
        checks if a credential exists 
        """
        for credentials in cls.user_information:
            if credentials.account_name == account_name:
                return True
        return False

@classmethod
def display_credentials(cls):
        """
        return all items in the credentials list
        """
        return cls.user_information

    
def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))

    
  





