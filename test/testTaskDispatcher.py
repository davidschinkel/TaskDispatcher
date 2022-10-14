from TaskDispatcher import *
import unittest

class testFullRun(unittest.TestCase):

    @staticmethod
    def assertTaskAndStudentsInGroup(group : StudentGroup, studentNames : list[str], task : Task):
        assert(group.task == task)
        assert(group.students[0].name == studentNames[0])
        assert(group.students[1].name == studentNames[1])
        assert(group.students[2].name == studentNames[2])

    def testTestdata1(self):
        students = SurveyParser().parseCSV("test/testdata1.dat")

        baStudents = Student.filterForStudentOfType(students, StudentType.BA)
        maStudents = Student.filterForStudentOfType(students, StudentType.MA)

        [baGroups, baOrphans] = TaskDispatcher(baStudents).dispatch()
        [maGroups, maOrphans] = TaskDispatcher(maStudents).dispatch()

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