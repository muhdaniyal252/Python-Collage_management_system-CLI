from data import students,get_ids

def list_all_students():
    return students

def list_students_by_ids(dta):
    ids = get_ids()
    return list(filter(lambda x: x._id in ids,dta))

def list_students_by_session_year(dta):
    year =  input('Sessional Year: ')
    return list(filter(lambda x: x.session_year == year,dta))

def list_students_by_field_id(dta):
    field_id = input('Field ID: ')
    return list(filter(lambda x: x.field_id == field_id,dta))

def student_operations():
    while True:
        print('1. Back')
        print('2. List all Students')
        print('3. List Students by IDs (comma saperated)')
        print('4. List Students by Anual Year')
        print('5. List Students Field ID')
        print('6. List Students Field ID and Sessional Year')
        choice = input('Choice: ')
        
        dta = list_all_students()

        if choice == '1':
            return
        elif choice == '2':
            pass
        elif choice == '3':
            dta = list_students_by_ids(dta)
        elif choice == '4':
            dta = list_students_by_session_year(dta)
        elif choice == '5':
            dta = list_students_by_field_id(dta)
        elif choice == '6':
            dta = list_students_by_session_year(dta)
            dta = list_students_by_field_id(dta)
        else:
            print('Incorrect Option')
            continue
        if not len(dta) > 0: 
            print('No Records Found') 
            continue
        print('ID, Name, Field ID, Sessional Year, Date of Admission')
        for i in dta:
            print(i._id, i.name, i.field_id, i.session_year, i.date,sep=', ')
