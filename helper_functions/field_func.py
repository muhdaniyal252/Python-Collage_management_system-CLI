from data import fields
from database.administration import Field

def field_CRUD():
    while True:
        print('1. Back')
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


def add_field():
    name = input('Name of Field: ')
    _id = 1 if len(fields) == 0 else sorted(fields,key=lambda x: x._id)[-1]._id + 1
    field = Field(_id, name)
    fields.append(field)
    print('Added Successfully')
    return

def list_fields():
    for i in fields:
        print(i._id, ': ', i.name)

def update_field():
    _id = input('Enter id to update (q if do not want to update): ')
    if _id == 'q':
        return
    _id = int(_id)
    for i in fields:
        if i._id == _id:
            name = input(f'Enter Field Name (current name is {i.name}, press enter to keep it as it is): ')
            i.name = name or i.name
            return
    print('Incorrect Id')
    return update_field()

def delete_field():
    _id = input('Enter id to delete (q if do not want to delete): ')
    if _id == 'q': return
    _id = int(_id)
    index = 0
    for idx,i in enumerate(fields):
        if i._id == _id:
            index = idx
            break
    if index:
        fields.pop(index)
        return
    print('Incorrect Id')
    return delete_field()
