"""
Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
"""

n = int(input())
my_tuple = tuple(map(int, input().split()))
print(hash(my_tuple))