from enum import Enum

class Task(Enum):
    Task1 = 1
    Task2 = 2
    Task3 = 3
    Task4 = 4
    Task5 = 5
    Task6 = 6
    Task7 = 7
    Task8 = 8
    Task9 = 9
    Task10 = 10

class Voting:
    def __init__(self, task : Task, value : int):
        self.task = task   
        self.value = value

    def __str__(self):
        return "task " + str(self.task) + " voting " + str(self.value)

    def __repr__(self):
        return str(self)