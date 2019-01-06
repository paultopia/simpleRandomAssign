# simpleRandomAssign

randomly assign assignments to students (or any list of things to any other list of things)

assumes list of assignments and list of cases are in text files with one per line

e.g. students.txt as in:

```
Schmoe, Joe
Schmusan, Susan
```

and cases.txt as in:

```
Brown v. Board of Education
Tinker v. Des Moines
```

then just redirect the output to a file etc.

```
python select_students.py students.txt cases.txt > assignments.md

pandoc -o assignments.html assignments.md

```
