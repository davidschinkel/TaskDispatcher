from enum import Enum
from voting import *

class StudentType(Enum):
    UNKNOWN = -1
    BA = 0
    MA = 1

class Student:

    def __init__(self, votings : list[Voting], studentType : StudentType, name : str):
        self.votings = votings
        self.studentType = studentType
        self.name = name
        self.votingForSorting = -1

    def votingForTask(self, task):
        
        for voting in self.votings:
            if voting.task == task:
                return voting.value

        return -1

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    @staticmethod
    def filterForStudentOfType(students : list, studentType : StudentType):
        return [student for student in students if student.studentType == studentType]