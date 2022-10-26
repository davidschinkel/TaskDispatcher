class StudentType():
    
    def __init__(self, studentType : str):
        self.description = str.strip(studentType)

    def __eq__(self, other):
        return self.description == other.description

    def __hash__(self):
        return hash(self.description)
