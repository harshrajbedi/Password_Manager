from user_menu import main_menu, add_password, find_password, search_email, delete_passwd
from master_password import get_master_passwd


unlock_key = input('Enter the MASTER PASSWORD: ')
MASTER_KEY = get_master_passwd()

if unlock_key == MASTER_KEY:
    print('Welcome to Password Manager')
else:
    print('Try again and enter the correct Master Password!')
    exit()


choice = main_menu()
while choice != 'Q':
    if choice == '1':
        add_password()
    if choice == '2':
        find_password()
    if choice == '3':
        search_email()
    if choice == '4':
        delete_passwd()
    else:
        choice = main_menu()
exit()
