

class Person:

    def __init__(self,_id,name,email,password,phone) -> None:
        self._id = _id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone



class Student(Person):

    def __init__(self, name, email, password, phone, field_id) -> None:
        super().__init__(name, email, password, phone)
        self.field_id = field_id
        


class Teacher(Person):

    def __init__(self, name, email, password, phone, subject_id) -> None:
        super().__init__(name, email, password, phone)
        self.subject_id  = subject_id
        

