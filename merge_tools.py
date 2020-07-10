"""Sample Input

AABCAAADA
3
Sample Output

AB
CA
AD
"""

# S, N = input(), int(input())
#
# for part in zip(*[iter(S)] * N):
#     d = dict()
#     print(''.join([d.setdefault(c, c) for c in part if c not in d]))


s = input()
k = int(input())
num_subsegments = int(len(s) / k)

for index in range(num_subsegments):

    t = s[index * k: (index + 1) * k]  # AAB CAA ADA , we have to traverse 3 segments a time
    u = ""

    for c in t:
        if c not in u:
            u += c
    print(u)
