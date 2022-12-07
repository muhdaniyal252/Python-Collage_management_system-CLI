import datetime

class Person:

    def __init__(self,_id,name,email,password,phone,date,*args) -> None:
        self._id = int(_id)
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        try: self.date = datetime.strptime(date,'%Y-%m-%d').date()
        except: self.date = date
        

    def get_header(self):
        return ['ID','Name','Email','Password','Phone','Date']


class Student(Person):

    def __init__(self,_id, name, email, password, phone, date, field_id, session_year, *args) -> None:
        super().__init__(_id, name, email, password, phone, date)
        self.field_id = field_id
        self.session_year = session_year

        


class Teacher(Person):

    def __init__(self, _id, name, email, password, phone, date, subject_id, *args) -> None:
        super().__init__(_id, name, email, password, phone, date)
        self.subject_id  = subject_id
        

