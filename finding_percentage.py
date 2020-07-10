n = int(input())
student_marks = {}

for _ in range(n):
    name, *marks = input().split()
    scores = list(map(float, marks))
    student_marks[name] = scores

student_name = input()

if student_name in student_marks:
    x = ((float(student_marks[student_name][0]) +
          float(student_marks[student_name][1]) +
          float(student_marks[student_name][2])) / 3)
    print('{:.2f}'.format(x))
