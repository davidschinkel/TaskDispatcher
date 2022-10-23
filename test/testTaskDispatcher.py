from taskDispatcher import *
from student import *

import unittest
import surveyParser

class testFullRun(unittest.TestCase):

    @staticmethod
    def assertTaskAndStudentsInGroup(group : StudentGroup, studentNames : list[str], task : Task):
        assert(group.task == task)
        assert(group.students[0].name == studentNames[0])
        assert(group.students[1].name == studentNames[1])
        assert(group.students[2].name == studentNames[2])

    def testTestdata1_reverseSorting_True(self):
        students = surveyParser.SurveyParser().parseCSV("test/testdata1.dat")

        baStudents = Student.filterForStudentOfType(students, StudentType.BA)
        maStudents = Student.filterForStudentOfType(students, StudentType.MA)

        [baGroups, baOrphans] = Dispatcher(baStudents).dispatch()
        [maGroups, maOrphans] = Dispatcher(maStudents).dispatch()

        assert(len(baGroups) == 3)
        testFullRun.assertTaskAndStudentsInGroup(baGroups[0], ["Student5", "Student8", "Student1"], Task.Task4)
        testFullRun.assertTaskAndStudentsInGroup(baGroups[1], ["Student3", "Student7", "Student10"], Task.Task5)
        testFullRun.assertTaskAndStudentsInGroup(baGroups[2], ["Student2", "Student4", "Student6"], Task.Task9)

        assert(len(baOrphans) == 1)
        assert(baOrphans[0].name == "Student9")

        assert(len(maGroups) == 3)
        testFullRun.assertTaskAndStudentsInGroup(maGroups[0], ["Student11", "Student19", "Student20"], Task.Task4)
        testFullRun.assertTaskAndStudentsInGroup(maGroups[1], ["Student13", "Student15", "Student16"], Task.Task6)
        testFullRun.assertTaskAndStudentsInGroup(maGroups[2], ["Student18", "Student17", "Student12"], Task.Task4)

        assert(len(maOrphans) == 1)
        assert(maOrphans[0].name == "Student14")

    def testTestdata1_reverseSorting_False(self):
        students = surveyParser.SurveyParser().parseCSV("test/testdata1.dat")

        baStudents = Student.filterForStudentOfType(students, StudentType.BA)
        maStudents = Student.filterForStudentOfType(students, StudentType.MA)

        [baGroups, baOrphans] = Dispatcher(baStudents, sortingReverse=False).dispatch()
        [maGroups, maOrphans] = Dispatcher(maStudents, sortingReverse=False).dispatch()

        assert(len(baGroups) == 3)
        testFullRun.assertTaskAndStudentsInGroup(baGroups[0], ["Student5", "Student7", "Student10"], Task.Task7)
        testFullRun.assertTaskAndStudentsInGroup(baGroups[1], ["Student3", "Student6", "Student8"], Task.Task6)
        testFullRun.assertTaskAndStudentsInGroup(baGroups[2], ["Student2", "Student4", "Student9"], Task.Task2)

        assert(len(baOrphans) == 1)
        assert(baOrphans[0].name == "Student1")

        assert(len(maGroups) == 3)
        testFullRun.assertTaskAndStudentsInGroup(maGroups[0], ["Student15", "Student19", "Student13"], Task.Task5)
        testFullRun.assertTaskAndStudentsInGroup(maGroups[1], ["Student11", "Student12", "Student14"], Task.Task9)
        testFullRun.assertTaskAndStudentsInGroup(maGroups[2], ["Student18", "Student17", "Student20"], Task.Task7)

        assert(len(maOrphans) == 1)
        assert(maOrphans[0].name == "Student16")