from data import teachers, get_ids

def list_all_teachers():
    return teachers

def list_teachers_by_ids(dta):
    ids = get_ids()
    return list(filter(lambda x: x._id in ids, dta))

def list_teacher_by_subject_id(dta):
    subject_id = input('Subject ID: ')
    return list(filter(lambda x: x.subject_id == subject_id,dta))


def teacher_operations():
    while True:
        print('1. Back')
        print('2. List all Teachers')
        print('3. List Teachers by IDs (comma saperated)')
        print('4. List Teachers Subject ID')
        choice = input('Choice: ')
        
        dta = list_all_teachers()

        if choice == '1':
            return
        elif choice == '2':
            pass
        elif choice == '3':
            dta = list_teachers_by_ids(dta)
        elif choice == '4':
            dta = list_teacher_by_subject_id(dta)
        else:
            print('Incorrect Option')
            continue
        if not len(dta) > 0: 
            print('No Records Found') 
            continue
        print('ID, Name, Subject ID, Date of Appointment')
        for i in dta:
            print(i._id, i.name, i.subject_id, i.date,sep=', ')
