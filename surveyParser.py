import csv
import logging
from task import *
from voting import *
from student import *
from studentType import *

class SurveyParser:

    def parseCSV(self, path : str):
        students=[]
        studentTypes=set()
        tasks=set()
        with open(path) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                    votings = []
                    name = row[0]
                    studentType = StudentType(row[1])

                    taskNumber = 1
                    for entry in row[2:]:
                        task = Task(taskNumber)
                        votings.append(Voting(task, int(entry)))
                        tasks.add(task)
                        taskNumber+=1

                    student = Student(votings, studentType, name)
                    logging.debug(student)
                    logging.debug(student.votings)
                    students.append(Student(votings, studentType, name))
                    studentTypes.add(studentType)
        return [students, studentTypes, tasks]