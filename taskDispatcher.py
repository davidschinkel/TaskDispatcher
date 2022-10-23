import logging
import argparse
from student import *
from dispatcher import *
from surveyParser import *


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

    [baGroups, baOrphans] = Dispatcher(baStudents, args.sortingReverse).dispatch()
    [maGroups, maOrphans] = Dispatcher(maStudents, args.sortingReverse).dispatch()

    #Printing of the results
    Dispatcher.printGroups(baGroups)
    Dispatcher.printOrphans(baOrphans)

    Dispatcher.printGroups(maGroups)
    Dispatcher.printOrphans(maOrphans)



    
        