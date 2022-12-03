from data import fields
from database.administration import Field

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
            i.name = input('Enter Field Name')
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
