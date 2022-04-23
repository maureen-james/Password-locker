import string
import random

class Credentials:
     """
     stores users credentials.
     
     """
     user_infomation = []

def __init__(self,account_name,password):
    self.acc_name=account_name
    self.password=password

def save_credentials(self):
    """
    saves users credentials
    """ 
    Credentials.user_infomation.append(self)  


