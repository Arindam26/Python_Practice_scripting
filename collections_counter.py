"""Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
"""
from collections import Counter

number_of_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()[:number_of_shoes]))
N = int(input())
earnings = 0
for customer in range(N):
    size, cost = map(int, input().split())
    if size in shoe_sizes and shoe_sizes[size] > 0:
        shoe_sizes[size] -= 1
        earnings += cost

print(earnings)


