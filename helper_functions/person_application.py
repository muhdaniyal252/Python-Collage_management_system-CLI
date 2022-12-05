from database.person_app import StudentApp,TeacherApp
from data import student_applications,teacher_applications,is_unique_email,get_id,application_status
from datetime import datetime

def get_person_details():
    print('Please enter asked detials')
    name = input('Full Name: ')
    email = input('Email: ')
    password = input('Password: ')
    phone = input('Phone: ')
    return (name,email,password,phone)

def student_application():
    (name,email,password,phone) = get_person_details()
    _id = get_id(student_applications)
    field_id = input('Field ID: ')
    date = datetime.now().date().today()
    status = application_status['2']
    if not is_unique_email(email):
        return
    stu_app = StudentApp(_id,name,email,password,phone,date,status,field_id)
    student_applications.append(stu_app)
    print('Applied Successfully!!!!')
    return

def teacher_application():
    (name,email,password,phone) = get_person_details()
    subject_id = input('Subject ID: ')
    if not is_unique_email(email):
        return
    _id = get_id(teacher_applications)
    date = datetime.now().date().today()
    status = application_status['1']
    thr_app = TeacherApp(_id,name,email,password,phone,date,status,subject_id)
    teacher_applications.append(thr_app)
    print('Applied Successfully!!!!')
    return