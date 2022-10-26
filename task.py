class Task:

    def __init__(self, number, description=''):
        self.number = number
        self.description = description

    def __eq__(self, other):
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)
    
    def __str__(self):
        return str(self.number)