import random
import string

class User:
     """
     stores users info.

     """
     user_info = []
     def __init__(self,f_name,p_number):
       self.f_name=f_name
       self.p_number=p_number
      
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
        method that returns the user list
        '''
        return cls.user_info