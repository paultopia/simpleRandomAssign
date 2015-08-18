import random, tabulate

# tabulate is not part of the standard library but is on pypi

def readingCheck(numReadings, readingList, origReadings):
    if not readingList:
        if origReadings:
            readingList = origReadings
        else:
            readingList = range(1, numReadings + 1)
    return readingList[:]

def pickAssignment(thisStud, mutReadings, numReadings, readingList):
    mutReadings = readingCheck(numReadings, mutReadings, readingList)
    choice = random.choice(mutReadings)
    mutReadings.remove(choice)
    if choice in thisStud:
        choice = pickAssignment(thisStud, mutReadings, numReadings, readingList)
    return (choice, mutReadings)


def randomMatch(numStud, numReadings, numPerStud, readingList = None, verbose = True):
    # readinglist, if exists, should just be nice list of names of readings.
    studentMatch = []
    mutReadings = readingList
    for studentNum in range(numStud):
        thisStud = [studentNum + 1]
        for count in range(numPerStud):
            theChoice = pickAssignment(thisStud, mutReadings, numReadings, readingList)
            thisStud.append(theChoice[0])
            mutReadings = theChoice[1]
        studentMatch.append(thisStud)
    if verbose:
        print tabulate.tabulate(studentMatch)
    return studentMatch
