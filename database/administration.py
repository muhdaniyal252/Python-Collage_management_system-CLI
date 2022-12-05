admins = []
# programs = []
# subjects = []



class Administration:

    def __init__(self,_id,name,email,password):
        self._id = int(_id)
        self.name = name
        self.email = email
        self.password = password

    def get_header(self):
        return ['ID','Name','Email','Password']



class Field:

    def __init__(self,_id,name):
        self._id = int(_id)
        self.name = name

    def get_header(self):
        return ['ID','Name']


class Subject:

    def __init__(self,_id,name,field_id):
        self._id = int(_id)
        self.name = name
        self.field_id = field_id

    def get_header(self):
        return ['ID','Name','Field ID']