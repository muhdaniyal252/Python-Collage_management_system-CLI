from database.person import Person
from datetime import datetime

class PersonApp(Person):

    def __init__(self, _id, name, email, password, phone,date,status,*args) -> None:
        super().__init__(_id, name, email, password, phone)
        try: self.date = datetime.strptime(date,'%Y-%m-%d').date()
        except: self.date = date
        self.status = status

    def get_header(self):
        header = super().get_header()
        header.append('Status')
        return header

class StudentApp(PersonApp):

    def __init__(self,_id, name, email, password, phone, date,status,field_id, *args) -> None:
        super().__init__(_id,name, email, password, phone,date,status)
        self.field_id = field_id
        self.status = 'Pending Test'

    def get_header(self):
        header = super().get_header()
        header.append('Field ID')
        return header

class TeacherApp(PersonApp):

    def __init__(self,_id, name, email, password, phone,date,status, subject_id, *args) -> None:
        
        super().__init__(_id,name, email, password, phone,date,status)
        self.subject_id  = subject_id
        
    def get_header(self):
        header = super().get_header()
        header.append('Subject ID')
        return header
