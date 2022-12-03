from database.administration import *
from database.person_app import *
from database.person import *
from helper_functions.admin_functions import *
from helper_functions.student_functions import *
from data import *



def main():
    while True:
        print('Welcome to Portal. \nPlease enter desired option')
        print('1. Login')
        print('2. Apply for Admission')
        print('3. Apply for Job')
        print('4. Save Data')
        choice = input('Choice: ')
        if choice == '1':
            adminportal()
            email = input('Enter Email: ')
            password = input('Enter Password: ')
            for i in admins:
                if i.email == email and i.password == password:
                    adminportal()
                    continue
                else: 
                    print('incorrect email or password')
        elif choice == '2':
            student_application_application()
        elif choice == '3':
            pass
        elif choice == '4':
            save_data()



if __name__ == '__main__': 
    get_data()
    main()