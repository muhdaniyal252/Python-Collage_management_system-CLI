from helper_functions.field_func import *

def adminportal():
    while True:
        print('Admin Portal')
        print('Welcome to Portal. \nPlease enter desired option')
        print('1. Logout')
        print('2. Add Field')
        print('3. List Fields')
        print('4. Update Field')
        print('5. Delete Field')
        choice = input('Choice: ')
        if choice == '1':
            return
        elif choice == '2':
            add_field()
        elif choice == '3':
            list_fields()
        elif choice == '4':
            update_field()
        elif choice == '5':
            delete_field()

