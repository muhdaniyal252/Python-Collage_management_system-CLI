from data import student_applications,teacher_applications
from datetime import datetime

def list_all_student_applications():
    return student_applications

def list_student_applications_by_status(dta, status):
    return list(filter(lambda x: x.status == status,dta))

def list_student_applicatoins_between_dates(dta, start_date,end_date):
    start_date = datetime.strptime(start_date,'%d-%m-%Y')
    end_date = datetime.strptime(end_date,'%d-%m-%Y')
    return list(filter(lambda x: (x.date >= start_date and x.date <= end_date),dta))

def list_student_applicatoins(dta):
    print('ID, Name, Field ID, Status')
    for i in dta:
        print(i._id, i.name, i.field_id, i.status)
    


def list_all_teacher_applications():
    return teacher_applications

def list_teacher_applications_by_status(dta, status):
    return list(filter(lambda x: x.status == status,dta))

def list_teacher_applications_between_dates(dta, start_date,end_date):
    start_date = datetime.strptime(start_date,'%d-%m-%Y')
    end_date = datetime.strptime(end_date,'%d-%m-%Y')
    return list(filter(lambda x: (x.date >= start_date and x.date <= end_date),dta))

def list_teacher_applicatoins(dta):
    print('ID, Name, Field ID, Status')
    for i in dta:
        print(i._id, i.name, i.subject_id, i.status)
    


