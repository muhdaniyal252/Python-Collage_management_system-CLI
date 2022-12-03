

class PersonApp:

    def __init__(self,_id,name,email,password,phone) -> None:
        self._id = _id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.status = 'Applied' 
                                # Pending Test
                                # Peding Interview
                                # Accepted
                                # Rejected


class StudentApp(PersonApp):

    def __init__(self, name, email, password, phone, field_id) -> None:
        super().__init__(name, email, password, phone)
        self.field_id = field_id
        


class TeacherApp(PersonApp):

    def __init__(self, name, email, password, phone, subject_id) -> None:
        super().__init__(name, email, password, phone)
        self.subject_id  = subject_id
        

