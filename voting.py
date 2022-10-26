from enum import Enum
from task import *

class Voting:
    def __init__(self, task : Task, value : int):
        self.task = task   
        self.value = value

    def __str__(self):
        return "task " + str(self.task) + " voting " + str(self.value)

    def __repr__(self):
        return str(self)