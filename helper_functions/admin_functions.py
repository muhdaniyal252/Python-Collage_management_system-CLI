from helper_functions.field_func import field_CRUD
from helper_functions.subject_func import subject_CRUD
from data import admins,is_unique_email,get_id
from database.administration import Administration
from helper_functions.application_func import teacher_applicatoin_operations,student_applicatoin_operations


def admin_CRUD():
    while True:
        print('1. Back')
        print('2. Add Admin')
        print('3. List Admins')
        print('4. Update Admin')
        print('5. Delete Admin')
        choice = input('Choice: ')
        if choice == '1':
            return
        elif choice == '2':
            add_admin()
        elif choice == '3':
            list_admins()
        elif choice == '4':
            update_admin()
        elif choice == '5':
            delete_admin()


def add_admin():
    name = input('Name of Admin: ')
    email = input('Email of Admin: ')
    password = input('Password of Admin: ')
    if not is_unique_email(email):
        return
    _id = get_id(admins)
    field = Administration(_id, name,email,password)
    admins.append(field)
    print('Added Successfully')
    return

def list_admins():
    for i in admins:
        print(i._id, ': ', i.name, ', ', i.email)

def update_admin():
    _id = input('Enter id to update (q if do not want to update): ')
    if _id == 'q':
        return
    _id = int(_id)
    for i in admins:
        if i._id == int(_id):
            name = input(f'Enter Field Name (current name is {i.name}, press enter to keep it as it is): ')
            i.name = name or i.name
            return
    print('Incorrect Id')
    return update_admin()

def delete_admin():
    _id = input('Enter id to delete (q if do not want to delete): ')
    if _id == 'q': return
    _id = int(_id)
    index = 0
    for idx,i in enumerate(admins):
        if i._id == int(_id):
            index = idx
            break
    if index:
        admins.pop(index)
        return
    print('Incorrect Id')
    return delete_admin()


def adminportal():
    while True:
        print('Admin Portal')
        print('Welcome to Portal. \nPlease enter desired option')
        print('1. Logout')
        print('2. Admin CRUD')
        print('3. Field CRUD')
        print('4. Subject CRUD')
        print('5. Teachers\' Applications')
        print('6. Students\' Applications')
        choice = input('Choice: ')
        if choice == '1':
            return
        elif choice == '2':
            admin_CRUD()
        elif choice == '3':
            field_CRUD()
        elif choice == '4':
            subject_CRUD()
        elif choice == '5':
            teacher_applicatoin_operations()
        elif choice == '6':
            student_applicatoin_operations()
