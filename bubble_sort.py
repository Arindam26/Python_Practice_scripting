# def bubble(n):
#     b = len(n) - 1
#     for i in range(b):
#         for j in range(b - i):
#             if n[j] > n[j + 1]:
#                 n[j], n[j + 1] = n[j + 1], n[j]
#     return n
#
#
# a = list(map(int, input().split()))
# print(bubble(a))


"""Bubble sort"""


def bubble(n):
    b = len(n) - 1
    for i in range(b):
        for j in range(b - i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]

    return n


a = list(map(int, input().split()))
print(bubble(a))
