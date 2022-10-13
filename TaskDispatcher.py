from enum import Enum
import logging
import csv

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


class StudentGroup:

    def __init__(self, students : list[Student], task : Task):
        self.students = students
        self.task = task

    def __str__(self):
        return "Task" + str(self.task) + " Students:" + str(self.students)

class TaskDispatcher:

    def __init__(self, students : list[Student]):
        self.students = students

    def getBestVotedTask(self, students : list[Student]):
        bestVoting = 0
        bestVotedTask = None
        for task in Task:
            actualVoting = sum([student.votingForTask(task) for student in students])
            if(actualVoting > bestVoting):
                bestVotedTask = task
                bestVoting = actualVoting

        return bestVotedTask

    def dispatch(self):
        groups = []
        while len(self.students) > 2:    
            task = self.getBestVotedTask(students)
            #TODO Replace by function call with argument
            for student in self.students:
                student.votingForSorting = student.votingForTask(task)
            sortedStudents = sorted(self.students, key= lambda student: student.votingForSorting, reverse=True)
            newGroup = StudentGroup([sortedStudents[0], sortedStudents[1], sortedStudents[2]], task)
            groups.append(newGroup)
            self.students.remove(sortedStudents[0])
            self.students.remove(sortedStudents[1])
            self.students.remove(sortedStudents[2])

        self.logGroups(groups)
        self.logOrphans()

    def logGroups(self, groups):
        for group in groups:
            print(group)

    def logOrphans(self):
        if len(self.students) > 0:
            print("Students without task")
            print(self.students)

class SurveyParser:

    def parseCSV(self, path : str):
        students=[]
        with open(path) as csvfile:
            votings = []
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                    name = row[0]
                    votings.append(Voting(Task.Task1, int(row[1])))
                    votings.append(Voting(Task.Task2, int(row[2])))
                    votings.append(Voting(Task.Task3, int(row[3])))
                    votings.append(Voting(Task.Task4, int(row[4])))
                    votings.append(Voting(Task.Task5, int(row[5])))
                    votings.append(Voting(Task.Task6, int(row[6])))
                    votings.append(Voting(Task.Task7, int(row[7])))
                    votings.append(Voting(Task.Task8, int(row[8])))
                    votings.append(Voting(Task.Task9, int(row[9])))
                    votings.append(Voting(Task.Task10, int(row[10])))
                    studentType = row[11]
                    student = Student(votings, studentType, name)
                    logging.debug(student)
                    logging.debug(student.votings)
                    students.append(Student(votings, studentType, name))
        return students


if __name__ == '__main__':
    logging.basicConfig(filename='logging.log', level=logging.DEBUG)
    students = SurveyParser().parseCSV('testdata.dat')

    TaskDispatcher(students).dispatch()



    
        