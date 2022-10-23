from student import * 

class StudentGroup:

    def __init__(self, students : list[Student], task : Task):
        self.students = students
        self.task = task

    def __str__(self):
        return "Task" + str(self.task) + " Students:" + str(self.students)