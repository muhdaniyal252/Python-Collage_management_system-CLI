from database.administration import Administration,Field
import csv

admins = list()
fields = list()

file_name = lambda x: f'data/{x}.csv'

def get_from_file(fname,obj,dta):
    with open(fname,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            o = obj(**row)
            dta.append(o)
    return dta


def get_data():
    get_from_file(file_name('admins'),Administration,admins)
    if len(admins) == 0:
        _id = 1 if len(admins) == 0 else sorted(admins,key=lambda x: x._id)[-1]._id + 1
        admin = Administration(_id,'fayyaz','fayyaz@gmail.com','abc')
        admins.append(admin)
    get_from_file(file_name('fields'),Field,fields)

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
    save_in_file(file_name('admins'),admins)
    save_in_file(file_name('fields'),fields)
