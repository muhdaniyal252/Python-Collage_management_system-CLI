from data import fields,subjects,get_id
from database.administration import Subject
from helper_functions.field_func import list_fields


def subject_CRUD():
    while True:
        print('1. Back')
        print('2. Add Subject')
        print('3. List Subjects')
        print('4. Update Subject')
        print('5. Delete Subject')
        choice = input('Choice: ')
        if choice == '1':
            return
        elif choice == '2':
            add_subject()
        elif choice == '3':
            list_subjects()
        elif choice == '4':
            update_subject()
        elif choice == '5':
            delete_subject()

def add_subject():
    list_fields()
    name = input('Name of Subject: ')
    field_id = input('ID of Field: ')
    _id = get_id(subjects)
    subject = Subject(_id, name, field_id)
    subjects.append(subject)
    print('Added Successfully')
    return

def list_subjects():
    for i in subjects:
        print(i._id, ': ', i.name)

def update_subject():
    _id = input('Enter id to update (q if do not want to update): ')
    if _id == 'q':
        return
    _id = int(_id)
    for i in subjects:
        if i._id == int(_id):
            name = input(f'Enter Subject Name (current name is {i.name}, press enter to keep it as it is): ')
            i.name = name or i.name
            field_id = input(f'Enter Field ID (current name is {i.field_id}, press enter to keep it as it is): ')
            i.field_id = field_id or i.field_id
            return
    print('Incorrect Id')
    return update_subject()

def delete_subject():
    _id = input('Enter id to delete (q if do not want to delete): ')
    if _id == 'q': return
    _id = int(_id)
    index = 0
    for idx,i in enumerate(fields):
        if i._id == int(_id):
            index = idx
            break
    if index:
        fields.pop(index)
        return
    print('Incorrect Id')
    return delete_subject()
