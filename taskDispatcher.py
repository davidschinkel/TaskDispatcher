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
    [students, studentTypes] = SurveyParser().parseCSV(args.path)

    for studentType in studentTypes:
        studentsOfType = Student.filterForStudentOfType(students, studentType)
        [groups, orphans] = Dispatcher(studentsOfType, args.sortingReverse).dispatch()
        print("Students of type " + studentType.description)
        Dispatcher.printGroups(groups)
        Dispatcher.printOrphans(orphans)



    
        