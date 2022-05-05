from database import send_passwd_to_db, find_passw_from_db, search_email_from_db, delete_from_db
from hashing import password
def main_menu():
    print(('-'*10) + 'USER MENU' + ('-'*10))
    print('1. Add a new password into database')
    print('2. Find an existing password using app name')
    print('3. Search email related to a password')
    print('4. Delete a password from database')
    print('Press Q to exit')
    return input(': ')

def add_password():
    global enc_passwd
    app_site_name = input('Enter the name of app or website: ')
    email_add = input('Enter the email address (if not applicable, leave blank): ')
    web_site = input('Enter the url of the site: ')
    if email_add == None:
        email_add = ''
    user_name = input('Enter username (if applicable, leave blank): ')
    if user_name == None:
        user_name = ''
    print('Press y to auto generate password otherwise n to enter password manually: ')
    auto_choice = input()
    if auto_choice == 'y':
        plaintext = input('Please provide a simple password used for hashing: ')
        print('Generating Password Please Wait...')
        print('Password Generated Successfully')
        hashed_passwd = password(plaintext, app_site_name, 12) #HASHING
        alphabets = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '123456789' + '(,._-*~"<>/|!@#$%^&)+='
        key = 20
        send_passwd = ""
        for letter in hashed_passwd:
            new_position = (alphabets.find(letter)+key)%len(alphabets)
            send_passwd += alphabets[new_position]
    else:
        passwd = input('Manual Password: ')
        key = 20
        send_passwd = ""
        alphabets = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '123456789' + '(,._-*~"<>/|!@#$%^&)+='
        for letter in passwd:
            new_position = (alphabets.find(letter)+key)%len(alphabets)
            send_passwd += alphabets[new_position]
    send_passwd_to_db(app_site_name, user_name, email_add, web_site, send_passwd)

def find_password():
     app_name = input('Please provide the name of the site or app you want to find the password to: ')
     find_passw_from_db(app_name)

def search_email():
    user_email = input('Please provide the email that you want to find accounts for: ')
    search_email_from_db(user_email)

def delete_passwd():
    del_pass = input('Please provide the name app that you want to delete password for: ')
    delete_from_db(del_pass)

