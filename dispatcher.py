import logging
from student import * 
from studentGroup import *

class Dispatcher:

    def __init__(self, students : list[Student], sortingReverse = True):
        self.students = students
        self.sortingReverse = sortingReverse

    @staticmethod
    def getBestVotedTask(students : list[Student], sortingReverse):
        bestVoting = None
        bestVotedTask = None
        for task in Task:
            actualVoting = sum([student.votingForTask(task) for student in students])
            if(Dispatcher.isVotingBetter(actualVoting, bestVoting, sortingReverse)):
                logging.debug("task:" + str(task) + " actual voting:" + str(actualVoting))
                bestVotedTask = task
                bestVoting = actualVoting

        return bestVotedTask

    @staticmethod
    def isVotingBetter(actualVoting : int, bestVoting : int, sortingReverse : bool):
        if bestVoting is None:
            return True
        elif sortingReverse:
            return actualVoting > bestVoting
        else:
            return actualVoting < bestVoting

    def dispatch(self):
        groups = []
        while len(self.students) > 2:    
            task = Dispatcher.getBestVotedTask(self.students, self.sortingReverse)
            #TODO Replace by function call with argument
            for student in self.students:
                student.votingForSorting = student.votingForTask(task)
            sortedStudents = sorted(self.students, key= lambda student: student.votingForSorting, reverse=self.sortingReverse)
            newGroup = StudentGroup([sortedStudents[0], sortedStudents[1], sortedStudents[2]], task)
            groups.append(newGroup)
            self.students.remove(sortedStudents[0])
            self.students.remove(sortedStudents[1])
            self.students.remove(sortedStudents[2])

        return [groups, self.students]

    @staticmethod
    def printGroups(groups):
        for group in groups:
            print(group)

    @staticmethod
    def printOrphans(students):
        if len(students) > 0:
            print("Students without task")
            print(students)