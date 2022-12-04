from database.administration import Administration,Field,Subject
import csv

admins = list()
fields = list()
subjects = list()


file_name = lambda x: f'data/{x}.csv'
admins_filename = file_name('admins')
fields_filename = file_name('fields')
subject_filename = file_name('subjects')


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
    get_from_file(admins_filename,Administration,admins)
    if len(admins) == 0:
        _id = 1 if len(admins) == 0 else sorted(admins,key=lambda x: x._id)[-1]._id + 1
        admin = Administration(_id,'fayyaz','fayyaz@gmail.com','abc')
        admins.append(admin)
    get_from_file(fields_filename,Field,fields)
    get_from_file(subject_filename,Field,fields)

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
