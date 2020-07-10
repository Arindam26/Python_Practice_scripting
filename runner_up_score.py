"""Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
"""
n = int(input())
k = list(map(int, input().split()))
result = max(k)
while max(k) == result:
    k.remove(max(k))
print(max(k))
