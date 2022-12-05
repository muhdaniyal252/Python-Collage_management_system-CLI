from helper_functions.admin_functions import adminportal
from helper_functions.person_application import student_application,teacher_application
from data import *


def login():
    email = input('Enter Email: ')
    password = input('Enter Password: ')
    for i in admins:
        if i.email == email and i.password == password:
            adminportal()
        else: 
            print('incorrect email or password')

def main():
    get_data()
    while True:
        print('Welcome to Portal. \nPlease enter desired option')
        print('1. Login')
        print('2. Apply for Admission')
        print('3. Apply for Job')
        print('4. Save Data')
        choice = input('Choice: ')
        if choice == '1':
            adminportal()
            login()
        elif choice == '2':
            student_application()
        elif choice == '3':
            teacher_application()
        elif choice == '4':
            save_data()



if __name__ == '__main__':
    main()