import csv
import logging
from voting import *
from student import *
from studentType import *

class SurveyParser:

    def parseCSV(self, path : str):
        students=[]
        studentTypes=set()
        with open(path) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                    votings = []
                    name = row[0]
                    studentType = StudentType(row[1])

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
                    studentTypes.add(studentType)
        return [students, studentTypes]