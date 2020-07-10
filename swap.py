"""Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2"."""


def swap_case(n):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in n])


print(swap_case(input()))
