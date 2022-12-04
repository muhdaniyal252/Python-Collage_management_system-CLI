from helper_functions.field_func import field_CRUD
from helper_functions.subject_func import subject_CRUD

def adminportal():
    while True:
        print('Admin Portal')
        print('Welcome to Portal. \nPlease enter desired option')
        print('1. Logout')
        print('2. Field CRUD')
        print('3. Subject CRUD')
        choice = input('Choice: ')
        if choice == '1':
            return
        elif choice == '2':
            field_CRUD()
        elif choice == '3':
            subject_CRUD()
