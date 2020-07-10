#
# import string
# alpha = string.ascii_lowercase
#
# n = int(input())
# L = []
#
# for i in range(n):
#     s = '-'.join(alpha[i:n])
#     L.append((s[::-1]+s[1:]))
#
# print('\n'.join(L[::-1]))

import string

char = string.ascii_lowercase

n = int(input("Enter a number for the rangoli: "))
L = []

for i in range(n):
    s = '-'.join(char[i:n])
    L.append((s[::-1] + s[1:]).center(4 * n - 3, '-'))

print('\n'.join(L[:0:-1] + L))
print('\n'.join(L[:0:-1] + L))
