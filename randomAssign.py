import random, tabulate

# tabulate is not part of the standard library but is on pypi

def readingCheck(numReadings, readingList):
    if readingList is None:
        readingList = range(1, numCases + 1)
    return readingList[:]

def randomMatch(numStud, numReadings, numPerStud, readingList = None, verbose = True):
    # readinglist, if exists, should just be nice list of names of readings.
    studentMatch = []
    mutReadings = readingCheck(numReadings, readingList)
    for studentNum in range(numStud):
        thisStud = [studentNum + 1]
        if len(mutReadings) < numPerStud:
            mutReadings = readingCheck(numReadings, readingList)
        for count in range(numPerStud):
            theChoice = random.choice(mutReadings)
            thisStud.append(theChoice)
            mutReadings.remove(theChoice)
        studentMatch.append(thisStud)
    if verbose:
        print tabulate.tabulate(studentMatch)
    return studentMatch

