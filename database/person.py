

class Person:

    def __init__(self,_id,name,email,password,phone,*args) -> None:
        self._id = int(_id)
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def get_header(self):
        return ['ID','Name','Email','Password','Phone']


class Student(Person):

    def __init__(self, name, email, password, phone, field_id, annual_year, *args) -> None:
        super().__init__(name, email, password, phone)
        self.field_id = field_id
        self.annual_year = annual_year

        


class Teacher(Person):

    def __init__(self, name, email, password, phone, subject_id, *args) -> None:
        super().__init__(name, email, password, phone)
        self.subject_id  = subject_id
        

