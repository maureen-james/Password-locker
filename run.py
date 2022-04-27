# from Credentials import Credentials
from User import User,Credentials
import random

def create_user_account(username, password):
    '''
     creates a user account
    '''
    new_User = User(username, password)
    return new_User
def save_User(User):
    '''
     save user  account
    '''
    User.save_User()
def save_credentials(credentials):
    '''
    save credential  account
    '''
    credentials.save_credentials
def find_User(username):
    '''
    method for find user using username
    '''
    return User.find_User(username)
def create_credentials(account_name, username, password):
    '''
    method credential details
    '''
    new_credentials = Credentials(account_name, username, password)
    return new_credentials
def save_credentials(credentials):
    '''
    save credentials
    '''
    credentials.save_credentials()
def display_credentials():
    '''
    method to display all the saved credential
    '''
    return Credentials.display_credentials()
def find_account(account_name,username,password):
    '''
    method to search for an account
    '''
    return Credentials.find_account(account_name,username,password)

def delete_credentials(account_name):
    '''
    method to delete account
    '''
    account_name.delete_credentials()
def main():
    # Dealing user class first
    print("Welcome to Password Locker! Please enter your name:  ")
    name = input ()
    print(f"{name}, Sign up to continue")
    print('\n')
    print("*" * 80)
    print("Reply with  : cc - Sign Up,  ex -exit ")
    print("*" * 80)
    while True:
        short_code = input().lower()
        if short_code == 'cc':
            print("Creating account...")
            print("Key in these details:")
            print("Username: ")
            username = input()
            print("Password: ")
            password = input()
            save_User(create_user_account(username, password))
            print('\n')
            print(f"{name}'s Account information: ")
            print(f"Username: {username} , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("*" * 80)
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the password locker ")
            print("*" * 80)
        elif short_code == "ca":
            print("Enter account details: ")
            print("Account Name(e.g:Twitter): ")
            account_name = input()
            print("username: ")
            username = input()
            print("Would you like a generated password?")
            if input()=="yes":
                letters= "ghijklmnopqrstuvwxyz0123456789FGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of password is {how_many}")
                lent = int(input())
                password = "".join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)
                save_credentials(create_credentials(account_name, username, password))
                print("Credential saved! Enter 'da' to see account")
                print("*" * 80)
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the password locker")
                print("*" * 80)
            elif input() == "no":
                print("Password: ")
                password=input()
                save_credentials(create_credentials(account_name, username, password))
                print("Credential saved! Enter 'da' to see account")
                print("*" * 80)
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the password locker ")
                print("*" * 80)
                save_User(create_credentials(account_name, username,password)) # create and save new password.
                save_credentials(create_credentials(account_name, username,password))
                print ('\n')
                print(f"New User {account_name} {username} created")
                print ('\n')
            else:
                print("i dont get it please use shortcode 'ca' and start again")
        elif short_code == "da":
            print(f"These are your credentials for {name}:")
            print("*" * 30)
            for Credentials in display_credentials():
                print(f"{Credentials.account_name}\n {Credentials.username}\n {Credentials.password}")
            else:
                print("*" * 30)
                print("If empty, you do not have any accounts saved")
        elif short_code == "fa":
            print("Key in  the account you are searching for (ie.'Facebook'): " )
            search_credential= input()
            if find_account(search_credential):
                search_acc = find_account(search_credential)
                print(f"{search_acc.account_name} {search_acc.username} { search_acc.password}")
            else: print("This account does not exist")
        elif short_code == "gp":
                letters= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of password is {how_many}")
                lent = int(input())
                password = "".join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)
        elif short_code == "de":
            print("Enter the account name of the Credential you want to delete")
            search_name = input().lower()
            if delete_credentials(search_name):
                search_credentials = delete_credentials(search_name)
                print("_"*50)
                search_credentials.delete_credentials()
                print('\n')
                print(f"Your stored credential for : {search_credential.account_name} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")
        elif short_code == 'ex':
            print("*"*30)
            print("logging out...")
            print('\n')
            print('\n')
            print("logged out")
            print("*"*30)
            break
        else:
            print("Invalid, please  use these short codes : ca - create a new account, da - display accounts, fa -find an account, de- delete account , gp - generate a random password , ex -logout")

if __name__ == '__main__':
    main()