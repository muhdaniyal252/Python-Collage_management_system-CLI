
import csv

admins = list()
fields = list()
subjects = list()
student_applications = list()
teacher_applications = list()
students = list()
teachers = list()

application_status = {
    '1': 'Applied',
    '2': 'Pending Test',
    '3': 'Pending Interview',
    '4': 'Accepted',
    '5': 'Failed'
} 

file_name = lambda x: f'data/{x}.csv'
admins_filename = file_name('admins')
fields_filename = file_name('fields')
subject_filename = file_name('subjects')
student_application_filename = file_name('student_applications')
teacher_application_filename = file_name('teacher_applications')
teachers_filename = file_name('teachers')
students_filename = file_name('students')


get_id = lambda y: 1 if len(y) == 0 else sorted(y,key=lambda x: x._id)[-1]._id + 1

def get_ids():
    ids = input('IDs (coma saperated): ')
    ids = ids.replace(' ', '')
    ids = ids.split(',')
    ids = list(map(int,ids))
    return ids


not_uniq = lambda: print('Email Already Exists!!!!')


def is_unique_email(email):
    for i in admins:
        if i.email == email:
            not_uniq()
            return False
    return True


def get_from_file(fname,obj,dta):
    try:
        with open(fname,'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                o = obj(*row)
                dta.append(o)
        return dta
    except: pass


def get_data():
    from database.administration import Administration,Field,Subject
    from database.person_app import StudentApp,TeacherApp
    from database.person import Teacher, Student
    get_from_file(admins_filename,Administration,admins)
    if len(admins) == 0:
        _id = get_id(admins)
        admin = Administration(_id,'Admin','admin@cms.com','admin')
        admins.append(admin)
    get_from_file(fields_filename,Field,fields)
    get_from_file(subject_filename,Subject,subjects)
    get_from_file(student_application_filename,StudentApp,student_applications)
    get_from_file(teacher_application_filename,TeacherApp,teacher_applications)
    get_from_file(teachers_filename,Teacher,teachers)
    get_from_file(students_filename,Student,students)

def save_in_file(fname,dta):
    if not len(dta) > 0: return
    try: dta = sorted(dta,key=lambda x: x._id)
    except: pass
    with open(fname,'w') as f:
        writer = csv.writer(f)
        header = dta[0].get_header()
        writer.writerow(header)
        for i in dta:
            d = [v for _,v in i.__dict__.items()]
            writer.writerow(d)

def save_data():
    save_in_file(admins_filename,admins)
    save_in_file(fields_filename,fields)
    save_in_file(subject_filename,subjects)
    save_in_file(student_application_filename,student_applications)
    save_in_file(teacher_application_filename,teacher_applications)
    save_in_file(students_filename,students)
    save_in_file(teachers_filename,teachers)

