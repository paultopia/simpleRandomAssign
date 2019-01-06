import random, sys
from tabulate import tabulate

def match_students_to_assignments(studentsfile, assignmentsfile):
    with open(studentsfile) as stu:
        students = [x.strip() for x in stu.readlines()]
    with open(assignmentsfile) as ass:
        assignments = [x.strip() for x in ass.readlines()]
    shuffle = []
    output = []
    for student in students:
        if len(shuffle) == 0:
            shuffle = random.sample(assignments, len(assignments))
        output.append((student, shuffle.pop()))
    return tabulate(output, tablefmt="grid")

if __name__ == "__main__":
    students = sys.argv[1]
    assignments = sys.argv[2]
    print(match_students_to_assignments(students, assignments))
