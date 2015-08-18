# simpleRandomAssign
Simple random assignment of stuff to other stuff.  (My use is for students and readings.)  Prints out a nice table
(with the aid of external tabulate package), plus returns a list of lists where each sublist list is
[assignee, assignment 1, assignment2, ... assignmentn]

usage: call randomMatch(numStud, numReadings, numPerStud, readingList = None, verbose = True)
where:
numStud is the number of assignees
numReadings is the number of things assigned
numPerStud is the number of things to assign to each student
readingList is the optional list of names for things to assign
and Verbose is a boolean to choose whether to print a pretty table or just return the list silently.

takes an assignee, and randomly assigns them numPerStud assignments.  recycles the list when it runs out.
(because it recycles the list when there aren't enough for a single student, it's possible that some assignments are
chosen zero times even if numStud * numPerStud > numReadings)

example, and not conincidentally the task for my own class.  I have 26 students, and a list of cases.  I want each student
to have to write a brief for two cases, and I want to assign them randomly.

cases = ["Brown v. Board of Education", "Loving v. Virginia", "Milliken v. Bradley", "Washington v. Davis",
"Fisher v. University of Texas", "United States v. Virginia", "Geduldig v. Aiello",
"San Antonio School District v. Rodriguez", "Romer v. Evans", "Obergefell v. Hodges",
"Griswold v. Connecticut", "Roe v. Wade", "Reynolds v. Sims", "Lochner v. New York", "McDonald v. Chicago",
"Lucas v. South Carolina Coastal Council", "Rust v. Sullivan", "Buckley v. Valeo",
"Bernstein v. Department of Justice", "Employment Division v. Smith", "Burwell v. Hobby Lobby",
"McCreary County v. ACLU", "Shelley v. Kraemer"]

assignments = randomMatch(26, len(cases), 2, cases, True)
