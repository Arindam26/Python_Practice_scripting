"""Given the names and grades for each student in a class of  students,
 store them in a nested list and print the name(s) of any student(s) having the second lowest grade."""

n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
