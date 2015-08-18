# simpleRandomAssign
Simple random assignment of stuff to other stuff.  (My use is for students and readings.)  Prints out a nice table
(with the aid of external tabulate package), plus returns a list of lists where each sub-list is
[assignee, assignment 1, assignment2, ... assignmentn]

usage: call randomMatch(numStud, numReadings, numPerStud, readingList = None, verbose = True)
where:
numStud is the number of assignees
numReadings is the number of things assigned
numPerStud is the number of things to assign to each student
readingList is the optional list of names for things to assign
and Verbose is a boolean to choose whether to print a pretty table or just return the list silently.

takes each assignee, and randomly assigns him/her numPerStud assignments.  recycles the list when it runs out.

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

prints something pretty like (depending on random element):

--  ----------------------------------------  ----------------------------------------
1  Rust v. Sullivan                          Loving v. Virginia
2  Griswold v. Connecticut                   Employment Division v. Smith
3  Shelley v. Kraemer                        Washington v. Davis
4  Lucas v. South Carolina Coastal Council   Geduldig v. Aiello
5  Bernstein v. Department of Justice        Obergefell v. Hodges
6  McDonald v. Chicago                       Reynolds v. Sims
7  Fisher v. University of Texas             Buckley v. Valeo
8  United States v. Virginia                 San Antonio School District v. Rodriguez
9  Milliken v. Bradley                       Burwell v. Hobby Lobby
10  Romer v. Evans                            Brown v. Board of Education
11  McCreary County v. ACLU                   Lochner v. New York
12  Roe v. Wade                               Brown v. Board of Education
13  Shelley v. Kraemer                        Buckley v. Valeo
14  Bernstein v. Department of Justice        Griswold v. Connecticut
15  Employment Division v. Smith              United States v. Virginia
16  Lochner v. New York                       Geduldig v. Aiello
17  Reynolds v. Sims                          McCreary County v. ACLU
18  McDonald v. Chicago                       Fisher v. University of Texas
19  Burwell v. Hobby Lobby                    Obergefell v. Hodges
20  San Antonio School District v. Rodriguez  Washington v. Davis
21  Roe v. Wade                               Lucas v. South Carolina Coastal Council
22  Loving v. Virginia                        Rust v. Sullivan
23  Romer v. Evans                            Milliken v. Bradley
24  Employment Division v. Smith              Romer v. Evans
25  Bernstein v. Department of Justice        Shelley v. Kraemer
26  Reynolds v. Sims                          Fisher v. University of Texas
--  ----------------------------------------  ----------------------------------------
