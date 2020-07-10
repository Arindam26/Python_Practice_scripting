# num = int(input())
# for i in range(num):
#     print(' ' * (num - i - 1) + '*' * (2 * i + 1))
#
# for j in range(num):
#     print(' ' * j + "*" * (2 * num - 2 * j - 1))

"""Triangle : rombus"""


def triangle_rombus(num):
    for i in range(num):
        print(' ' * (num - i - 1) + '*' * (2 * i + 1))

    for j in range(num):
        print(' ' * j + '*' * (2 * num - 2 * j - 1))


star = int(input("Enter the number of rows: "))
triangle_rombus(star)
