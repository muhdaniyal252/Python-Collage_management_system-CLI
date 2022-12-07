from data import student_applications,teacher_applications,application_status,students,teachers,get_id,get_ids
from datetime import datetime
from database.person import Student,Teacher

def get_choice():
    print('1. Back')
    print('2. List all Applications')
    print('3. List Applications by status')
    print('4. List Applications between dates')
    print('5. List Applications between dates and by status')
    print('6. Proceed Application Status')
    choice = input('Choice: ')
    return choice

def get_status():
    print(application_status)
    choice = input('Choice: ')
    status = application_status.get(choice)
    return status


def list_all_student_applications():
    return student_applications

def list_student_applications_by_status(dta):
    status = get_status()
    return list(filter(lambda x: x.status == status,dta))

def list_student_applicatoins_between_dates(dta):
    start_date = input('Start Date dd-mm-yyyy: ')
    end_date = input('End Date dd-mm-yyyy: ')
    start_date = datetime.strptime(start_date,'%d-%m-%Y').date()
    end_date = datetime.strptime(end_date,'%d-%m-%Y').date()
    return list(filter(lambda x: (x.date >= start_date and x.date <= end_date),dta))

def proceed_student_application():
    ids = get_ids()
    status = get_status()
    applications = list_all_student_applications()
    applications = filter(lambda x: x._id in ids,applications)
    for i in applications:
        i.status = status
    if status == application_status.get('4'):
        _id = get_id(students)
        date = datetime.now().date().today()
        for i in applications:
            st = Student(_id,i.name,i.email,i.password,i.phone,date,i.field_id,'2022-2024')
            students.append(st)
            _id += 1

def student_applicatoin_operations():
    while True:
        print('STUDENT')
        choice = get_choice()
        dta = list_all_student_applications()
        if choice == '1':
            return
        elif choice == '2':
            pass
        elif choice == '3':
            dta = list_student_applications_by_status(dta)
        elif choice == '4':
            dta = list_student_applicatoins_between_dates(dta)
        elif choice == '5':
            dta = list_student_applications_by_status(dta)
            dta = list_student_applicatoins_between_dates(dta)
        elif choice == '6':
            proceed_student_application()
        else:
            print('Incorrect Option')
            continue
        if not len(dta) > 0: 
            print('No Records Found') 
            continue
        print('ID, Name, Field ID, Status, Date')
        for i in dta:
            print(i._id, i.name, i.field_id, i.status, i.date,sep=', ')


def list_all_teacher_applications():
    return teacher_applications

def list_teacher_applications_by_status(dta):
    status = get_status()
    return list(filter(lambda x: x.status == status,dta))

def list_teacher_applications_between_dates(dta):
    start_date = input('Start Date dd-mm-yyyy: ')
    end_date = input('End Date dd-mm-yyyy: ')
    start_date = datetime.strptime(start_date,'%d-%m-%Y').date()
    end_date = datetime.strptime(end_date,'%d-%m-%Y').date()
    return list(filter(lambda x: (x.date >= start_date and x.date <= end_date),dta))

def proceed_teacher_application():
    ids = get_ids()
    status = get_status()
    applications = list_all_teacher_applications()
    applications = filter(lambda x: x._id in ids,applications)
    for i in applications:
        i.status = status
    if status == application_status.get('4'):
        _id = get_id(teachers)
        date = datetime.now().date().today()
        for i in applications:
            th = Teacher(_id,i.name,i.email,i.password,i.phone,date,i.subject_id)
            teachers.append(th)
            _id += 1
            

def teacher_applicatoin_operations():
    while True:
        print('TEACHER')
        choice = get_choice()
        dta = list_all_teacher_applications()
        if choice == '1':
            return
        elif choice == '2':
            pass
        elif choice == '3':
            dta = list_teacher_applications_by_status(dta)
        elif choice == '4':
            dta = list_teacher_applications_between_dates(dta)
        elif choice == '5':
            dta = list_teacher_applications_by_status(dta)
            dta = list_teacher_applications_between_dates(dta)
        elif choice == '6':
            proceed_teacher_application()
        else:
            print('Incorrect Option')
            continue
        if not len(dta) > 0: 
            print('No Records Found') 
            continue
        print('ID, Name, Field ID, Status, Date')
        for i in dta:
            print(i._id, i.name, i.subject_id, i.status, i.date, sep=', ')
    
