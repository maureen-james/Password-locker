class User:
     """
     stores users info.

     """
     user_info = []
     def __init__(self,f_name,l_name,p_number):
       self.f_name=f_name
       self.l_name=l_name
       self.p_number=p_number
      
     def save_user(self):
      """
      saves user infomation.
      """  
      User.user_info.append(self)