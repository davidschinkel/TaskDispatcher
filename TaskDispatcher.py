from enum import Enum
import logging
import csv
import argparse

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

class StudentType(Enum):
    UNKNOWN = -1
    BA = 0
    MA = 1

class Voting:
    def __init__(self, task : Task, value : int):
        self.task = task   
        self.value = value

    def __str__(self):
        return "task " + str(self.task) + " voting " + str(self.value)

    def __repr__(self):
        return str(self)

class Student:

    def __init__(self, votings : list[Voting], studentType : StudentType, name : str):
        self.votings = votings
        self.studentType = studentType
        self.name = name
        self.votingForSorting = -1

    def votingForTask(self, task):
        filteredVotings =  filter(lambda voting: voting.task == task, self.votings)

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


class StudentGroup:

    def __init__(self, students : list[Student], task : Task):
        self.students = students
        self.task = task

    def __str__(self):
        return "Task" + str(self.task) + " Students:" + str(self.students)

class TaskDispatcher:

    def __init__(self, students : list[Student], sortingReverse = True):
        self.students = students
        self.sortingReverse = sortingReverse

    @staticmethod
    def getBestVotedTask(students : list[Student], sortingReverse):
        bestVoting = None
        bestVotedTask = None
        for task in Task:
            actualVoting = sum([student.votingForTask(task) for student in students])
            if(TaskDispatcher.isVotingBetter(actualVoting, bestVoting, sortingReverse)):
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
            task = TaskDispatcher.getBestVotedTask(self.students, self.sortingReverse)
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

class SurveyParser:

    def parseCSV(self, path : str):
        students=[]
        with open(path) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                    votings = []
                    name = row[0]
                    if int(row[1]) == 0:
                        studentType = StudentType.BA
                    elif int(row[1]) == 1:
                        studentType = StudentType.MA
                    else: 
                        studentType = StudentType.UNKNOWN

                    votings.append(Voting(Task.Task1, int(row[2])))
                    votings.append(Voting(Task.Task2, int(row[3])))
                    votings.append(Voting(Task.Task3, int(row[4])))
                    votings.append(Voting(Task.Task4, int(row[5])))
                    votings.append(Voting(Task.Task5, int(row[6])))
                    votings.append(Voting(Task.Task6, int(row[7])))
                    votings.append(Voting(Task.Task7, int(row[8])))
                    votings.append(Voting(Task.Task8, int(row[9])))
                    votings.append(Voting(Task.Task9, int(row[10])))
                    votings.append(Voting(Task.Task10, int(row[11])))

                    student = Student(votings, studentType, name)
                    logging.debug(student)
                    logging.debug(student.votings)
                    students.append(Student(votings, studentType, name))
        return students


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A tiny code to group students to assignments')
    parser.add_argument('path', metavar='path', type=str,
                    help='Path to file containing the votings')
    parser.add_argument('--sortAscending', dest='sortingReverse', action='store_false', help='If the lowest voting stands for the highest approval.')
    parser.add_argument('--sortDescending', dest='sortingReverse', action='store_true', help='If the highest voting stands for the highest approval. This is the default.')
    parser.set_defaults(sortingReverse=True)

    args = parser.parse_args()

    logging.basicConfig(filename='logging.log', level=logging.DEBUG)
    students = SurveyParser().parseCSV(args.path)

    baStudents = Student.filterForStudentOfType(students, StudentType.BA)
    maStudents = Student.filterForStudentOfType(students, StudentType.MA)

    [baGroups, baOrphans] = TaskDispatcher(baStudents, args.sortingReverse).dispatch()
    [maGroups, maOrphans] = TaskDispatcher(maStudents, args.sortingReverse).dispatch()

    #Printing of the results
    TaskDispatcher.printGroups(baGroups)
    TaskDispatcher.printOrphans(baOrphans)

    TaskDispatcher.printGroups(maGroups)
    TaskDispatcher.printOrphans(maOrphans)



    
        